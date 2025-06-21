FROM gitpod/workspace-full

RUN pip install --upgrade pip \
    && pip install flask requests
