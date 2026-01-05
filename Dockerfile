
FROM ghcr.io/astral-sh/uv:python3.13-bookworm AS builder
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

WORKDIR /code

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

COPY . .

# Sync dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen


FROM python:3.13-slim-bookworm

COPY --from=builder /code /code

COPY entrypoint.sh /usr/cli/entrypoint.sh
RUN chmod +x /usr/cli/entrypoint.sh

ENV PATH="/code/.venv/bin:$PATH"

ENTRYPOINT ["/usr/cli/entrypoint.sh"]
