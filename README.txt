http://tutorial.djangogirls.org/it/django_admin/index.html
Il comando che permette la creazione di un ambiente virtuale e' :
		python -m venv djangoprova
BASH COMMAND: 	
		whoami
		tree
		touch nome del file 						#crea un file
		
		pip install django==1.8
		python -m venv cartella-progetto			#crea un ambiente virtuale di python
		myenv/bin/Active.bat						#attiva un ambiente virtuale
		django-admin startproject nome-del-sito .	#notare il "." Questo crea una 
		pip install nome-della-libreria
		python manage.py migrate 					#crea un db con sqllite di default
		python manage.py makemigrations nomeapp 	#crea un file di migrazione
		python manage.py migrate nomeapp			#aggiorna il db nomeapp
		python manage.py runserver					#lancia il server
		python manage.py startapp nomeapp			#genera un app
		python manage.py createsuperuser			#setta il superuser

		
		//pythonanywhere
		git clone ... 	
		cd nome-della-directory-clonata
		virtualenv --python=python3.4 myvenv		#crea un ambiente virtuale su pythonanywhere
		source myvenv/bin/activate					# //
		pip install django==1.8 whitenoise==2.0		# //

		python manage.py collectstatic				# comando che unisce tutti i file statici sotto una singola cartella
		python manage.py migrate					#riesto anche da pythonanywhere
		python manage.py createsuperuser			#devo ricreare il superuser su pythonanywhere
		
		
Sono arrivato alla sezione 12