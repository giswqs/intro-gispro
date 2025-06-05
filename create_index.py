import os


def generate_index_html(directories, output_file):
    # Start the HTML content
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Directory Listing</title>
</head>
<body>
    <h1>Directory Listing</h1>
    <ul>
"""

    for directory in directories:
        if os.path.isdir(directory):
            html_content += f"<li><strong>{directory}</strong></li><ul>"
            all_files = []
            for root, dirs, files in os.walk(directory):
                for filename in files:
                    if root.startswith("./.git"):
                        continue
                    file_path = os.path.join(root, filename)
                    all_files.append(file_path)

            # Sort files alphabetically
            all_files.sort()

            for file_path in all_files:
                # Get the relative path to the file from the base directory
                relative_path = os.path.relpath(file_path, start=directory)
                html_content += f'<li><a href="{directory}/{relative_path}">{relative_path}</a></li>'
            html_content += "</ul>"

    # Close the HTML content
    html_content += """
    </ul>
</body>
</html>
"""

    # Write the HTML content to the output file
    with open(output_file, "w") as f:
        f.write(html_content)


# Specify the directories to list
directories_to_list = ["."]
# Specify the output HTML file
output_html_file = "index.html"

generate_index_html(directories_to_list, output_html_file)
