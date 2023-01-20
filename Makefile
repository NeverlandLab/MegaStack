init:
	python ./manage.py makemigrations &&\
	python ./manage.py migrate

init-admin:
	python manage.py createsuperuserwithpassword \
        --username admin \
        --password admin \
        --email admin@example.org \
        --preserve


celery-worker:
	celery -A MegaStack worker --loglevel=info --concurrency=1

celery-beat:
	celery -A MegaStack beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

run:
	daphne -b 0.0.0.0 -p 8000 mega_stack.asgi:application

test:
	pytest -v -p no:warnings --html=report.html --alluredir=allure

collect-static:
	python ./manage.py collectstatic --noinput

release-docker:
	docker build -t ccr.ccs.tencentyun.com/megalab/mega-stack-openresty . -f ./support-files/docker/megastack-openresty/Dockerfile
	docker build -t ccr.ccs.tencentyun.com/megalab/mega-stack . -f ./support-files/docker/megastack/Dockerfile
	docker push ccr.ccs.tencentyun.com/megalab/mega-stack
	docker push ccr.ccs.tencentyun.com/megalab/mega-stack-openresty
