import csv
from django.core.management.base import BaseCommand
from ...models import InstitutosConLicencia

class Command(BaseCommand):

    help ='Carga datos desde un achivo CSV a un modulo'

    def add_arguments(self,parser):
        parser.add_argument('csv_file',type=str,help='Path to the CSV file')

    def handle(self,*args,**kwargs):
        csv_file=kwargs['csv_file']
        with open(csv_file,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                instituto = InstitutosConLicencia(region=row[0],name=row[1],personJuridica=row[2],                        sedeLocal=row[3],direccion=row[4],programasLicenciados=row[5],nivel=row[6],modalidad=row[7])
                instituto.save()
