from motoristaCLI import MotoristaCLI
from motoristaDAO import MotoristaDAO
from database import Database

if __name__ == "__main__":
    db = Database("app_motoristas", "Motoristas")
    motorista_dao = MotoristaDAO(db)
    cli = MotoristaCLI(motorista_dao)
    cli.run()