def filter_postgres_log(file_path):
    error_levels = ['ERROR', 'FATAL', 'PANIC']

    with open(file_path, 'r') as log_file:
        for line in log_file:
            for level in error_levels:
                if level in line:
                    print(line.strip())

if __name__ == "__main__":
    logfile_path = "/app/postgres.log"  # Ruta completa del archivo de registro dentro del contenedor
    filter_postgres_log(logfile_path)
