# 1. Base image
FROM giswqs/pygis:latest

# 2. Metadata (optional)
LABEL maintainer="giswqs@gmail.com"

# 3. Set working directory and switch to root for setup
USER root
WORKDIR /app

# 4. Copy files and set permissions
COPY book/ /app/book/
RUN chown -R $NB_UID:$NB_GID /app/book && chmod -R u+w /app/book

# ✅ Make entire /app directory owned by the notebook user
RUN mkdir -p /app/workspace && \
    chown -R $NB_UID:$NB_GID /app && \
    chmod -R u+w /app

# 5. Switch to notebook user
USER $NB_UID

# 6. Set default working directory (optional)
WORKDIR /app

# 7. Command to run container
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]

# 8. Mount workspace directory and run container
# docker run -it -p 8888:8888 -v $(pwd):/app/workspace giswqs/pygis:book

# 9. To build the docker image
# docker buildx build --platform linux/amd64,linux/arm64 -t giswqs/pygis:book --push .