docker run --rm -it --name mega-stack-migrate --env-file ./.env ccr.ccs.tencentyun.com/megalab/mega-stack \
    python manage.py createsuperuserwithpassword \
        --username admin \
        --password admin \
        --email admin@example.org \
        --preserve