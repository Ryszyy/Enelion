To run the app

    git clone https://github.com/Ryszyy/Enelion.git
    cd Enelion
    
    export FLASK_APP="/path/to/run.py"
    flask db init
    flask db migrate
    flask db upgrade
    
    docker-compose build
    docker-compose up
