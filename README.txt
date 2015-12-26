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
		
		
		//console Django
		python manage.py shell							#permette di entrare nella console di django
		from nomeapp.models import nome-classe-oggetto	#permette di importare la classe a cui si vuole accedere
		nome-classe-oggetto.objects.all()				#prendo tutti gli oggetti di quella classe
		nome-classe-oggetto.objects.create(...)			#permette di creare un nuovo oggetto da shell
		nome-classe-oggetto.objects.filter(...)			#permette di filtrare all interno della tabella
		nome-classe-oggetto.objects.order_by(...)		#permette di ordinare gli oggetti
		oggetto-da-pubblicare.publish()
		
		
		
		
		
Sono arrivato alla sezione 17