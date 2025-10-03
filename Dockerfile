FROM spymovil/python38_imagen_base:20250930

# Evitar que Python haga buffering en stdout/stderr
ENV PYTHONUNBUFFERED=1

WORKDIR /apiredis
COPY . .
RUN ls -laR
RUN chmod 777 /apiredis/*

# Comando de arranque (-u también fuerza no buffer)
#CMD ["python3", "-u", "/bdbackup/app.py"]
#CMD ["python3", "/apiredis/app.py"]

# Asegúrate de que entrypoint sea ejecutable
RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]

EXPOSE 5100