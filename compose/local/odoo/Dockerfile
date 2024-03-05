FROM odoo@sha256:3f22c6e279d68f6f99e7c06127de42dcd49df9091a26905355d42571f1ba397e

USER root

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    python3 \
  # dependencies for building Python packages
    build-essential \
    # installing ps
    procps \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

COPY ./compose/local/odoo/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint
RUN chown odoo /entrypoint

COPY ./compose/local/odoo/odoo.conf /etc/odoo/
RUN sed -i 's/\r$//g' /etc/odoo/odoo.conf
RUN chmod +x /etc/odoo/odoo.conf
RUN chown odoo /etc/odoo/odoo.conf

COPY ./compose/local/odoo/commands/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
RUN chown odoo /start

COPY ./compose/local/odoo/commands/init /init
RUN sed -i 's/\r$//g' /init
RUN chmod +x /init
RUN chown odoo /init

RUN chmod +x ./
RUN chown odoo ./

COPY . /app

RUN chown -R odoo /app

# Set default user when running the container
USER odoo

ENTRYPOINT ["/entrypoint"]
