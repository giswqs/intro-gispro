# 1. Base image
FROM ghcr.io/opengeos/geospatial:latest

# 2. Metadata (optional)
LABEL maintainer="giswqs@gmail.com"

# 3. Set working directory and switch to root for setup
USER root
WORKDIR /app

# 4. Copy files and set permissions
COPY book/ /app/book/
RUN chown -R $NB_UID:$NB_GID /app/book && chmod -R u+w /app/book

# 5. Create workspace and set permissions
RUN mkdir /app/workspace && chown -R $NB_UID:$NB_GID /app/workspace

# 6. Switch to notebook user
USER $NB_UID

# 7. Set default working directory (optional)
WORKDIR /app

# 8. Command to run container
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]

# 9. Mount workspace directory and run container
# docker run -it -p 8888:8888 -v $(pwd):/app/workspace giswqs/gispro:latest