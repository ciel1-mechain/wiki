# Useful Docker Commands Reference

---

## Docker Images

| Command                      | Description                                         |
|------------------------------|-----------------------------------------------------|
| `docker images`              | List all Docker images (old syntax)                  |
| `docker image ls`            | List all Docker images (new syntax)                  |
| `docker image ls <name>`     | List images filtered by name                          |
| `docker rmi <image>`         | Remove a Docker image                                 |
| `docker build -t name .`     | Build an image from a Dockerfile in current folder   |

---

## Docker Containers

| Command                          | Description                                         |
|----------------------------------|-----------------------------------------------------|
| `docker ps`                     | List running containers                              |
| `docker ps -a`                  | List all containers (running + stopped)             |
| `docker ps -q`                  | Show only container IDs                              |
| `docker run --rm ...`           | Run a container and remove it after exit (ephemeral)|
| `docker run -it ...`            | Run container interactively (with shell)             |
| `docker stop <container>`       | Stop a running container                             |
| `docker rm <container>`         | Remove a stopped container                           |
| `docker logs <container>`       | Show logs of a container                             |
| `docker exec -it <container> sh/bash` | Open a shell inside a running container         |

---

## Cleaning Up (Non-image files)

| Command                      | Description                                         |
|------------------------------|-----------------------------------------------------|
| `docker container prune`     | Remove all stopped containers                        |
| `docker volume prune`        | Remove dangling/unused volumes                       |
| `docker network prune`       | Remove unused Docker networks                        |
| `docker builder prune`       | Remove Docker build cache                            |
| `docker system prune`        | Remove stopped containers, unused volumes/networks, dangling images, and build cache (use with caution) |

---

## Docker Miscellaneous

| Command                  | Description                                         |
|--------------------------|-----------------------------------------------------|
| `docker --version`       | Show Docker version                                 |
| `docker info`            | Show system-wide info about Docker setup           |
| `docker system df`       | Show disk usage by Docker images, containers, volumes |

---

## Tips

- Use `--rm` with `docker run` for temporary containers to avoid clutter.
- Build custom images with Dockerfile to install extra packages (e.g., `mkdocs-video`).
- Use `docker exec` to interactively access running containers.
- Prefer `docker image ls` over the older `docker images` where supported.

---


