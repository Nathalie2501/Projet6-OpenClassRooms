#################################################################################
#      Installation des logiciels de base Version 2                             #
#             Octobre 2021                                                      #
#            Nathalie FERRER                                                    #
#          #!/usr/bin/env python3                                               #
#################################################################################
#importation du module "os" => interagit avec système d'exploitation
import os
#manipulation courante des chemins
import os.path                                                                                              
import webbrowser
#utilisation du protocole http
import requests
#module qui fournit des outils pour créer, écrire, ajouter des données et lister un fichier ZIP.
import zipfile
#Ce module crée des fichiers et répertoires temporaires.
import tempfile
#pour les opérations sur les fichiers
import shutil
import time 



#Définition de la variable url => adresse aws qui contient le zip (ouvert à tous)
url = 'https://installation-logiciel.s3.eu-west-3.amazonaws.com/2.Win_install.zip'
#chemin cible
target_path = 'logiciels.zip'

print("///////////FICHIER ZIP RECUPERE DE AWS///////////")
#construction de l'objet requests qui va être envoyé au serveur pour récupérer les ressources (url)
response = requests.get(url, stream=True)
#Manipulation du fichier zip (extraction du fichier logiciels.zip)
handle = open(target_path, "wb")
for chunk in response.iter_content(chunk_size=512):
    # filtre les morceaux
    if chunk:  
        handle.write(chunk)
handle.close()

with zipfile.ZipFile("logiciels.zip","r") as zip_ref:
    zip_ref.extractall("targetdir")

print("///////////EXTRACTION DE LOGICIELS.ZIP OK///////////")

#definition des fonctions de test (logiciels présents ou pas - installation ou pas)
def test_openoffice():
    #méthode utilisée pour changer le répertoire de travail actuel                                                                                 
    os.chdir(r"C:\Program Files (x86)")
    #test à l'aide du module "os.path" et "exists" si dans la liste1, à l'argument "0", openoffice existe                                                                
    if(os.path.exists(liste1[0])):                                                               
        print("///////////OPENOFFICE EXISTE DÉJA///////////")   
    else:
        print("///////////INSTALLATION OPENOFFICE EN COURS///////////")
        #os.chdir(r"C:\Users\Nathalie\Downloads\targetdir\2.Win_install")
        path = os.path.realpath(__file__)
        os.chdir(path)
        #méthode utilisé pour interagir avec le systeme d'exploitation
        os.system("Apache_OpenOffice_4.1.8_Win_x86_install_fr.exe /S")
        print("///////////OPENOFFICE INSTALLÉ///////////")                                                         


def test_filezilla():
    os.chdir(r"C:\Users\Nathalie\AppData\Roaming")
    if(os.path.exists(liste1[1])):
        print("///////////FILEZILLA EXISTE DÉJA///////////")
    else:
        print("///////////INSTALLATION FILEZILLA EN COURS///////////")
        os.chdir(r"C:\Users\Nathalie\Downloads\targetdir\2.Win_install")
        os.system("FileZilla_3.56.0_win64-setup.exe /S")
        print("///////////FILEZILLA INSTALLÉ///////////")

def test_taskcoach():
    os.chdir(r"C:\Program Files (x86)")
    if(os.path.exists(liste1[2])):
        print("///////////TASKCOACH EXISTE DÉJA///////////")
    else:
        print("///////////INSTALLATION TASKCOACH EN COURS///////////")
        os.chdir(r"C:\Users\Nathalie\Downloads\targetdir\2.Win_install")
        os.system("task-coach_1-4-6_fr_67436.exe /S")
        print("///////////TASKCOACH INSTALLÉ///////////")
        

def test_vscode():
    os.chdir(r"C:\Program Files")
    if(os.path.exists(liste1[3])):
        print("///////////VSCODE EXISTE DÉJA///////////")
    else:
        print("///////////INSTALLATION VSCODE EN COURS///////////")
        os.chdir(r"C:\Users\Nathalie\Downloads\targetdir\2.Win_install")
        os.system("VSCodeUserSetup-x64-1.61.0.exe /qn")
        print("///////////VSCODE INSTALLÉ///////////")

def test_xampp():
    os.chdir(r"C:")
    if(os.path.exists(liste1[4])):
        print("///////////XAMPP EXISTE DÉJA///////////")
    else:
        print("///////////INSTALLATION XAMPP EN COURS///////////")
        os.chdir(r"C:\Users\Nathalie\Downloads\targetdir\2.Win_install")
        os.system("xampp-windows-x64-8.0.11-2-VS16-installer.exe")
        print("///////////XAMPP INSTALLÉ///////////")

def test_adobe_reader():
    os.chdir(r"C:\Program Files (x86)")
    if(os.path.exists(liste1[5])):
        print("///////////ADOBE READER EXISTE DÉJA///////////")
    else:
        print("///////////INSTALLATION ADOBE READER EN COURS///////////")
        os.chdir(r"C:\Users\Nathalie\Downloads\targetdir\2.Win_install")
        os.system("readerdc_fr_xa_crd_install.exe")
        print("///////////ADOBE READER INSTALLÉ///////////")


def test_skype():
    os.chdir(r"C:\Users\Nathalie\AppData\Roaming")
    if(os.path.exists(liste1[6])):
        print("///////////SKYPE EXISTE DÉJA///////////")
    else:
        print("///////////INSTALLATION SKYPE EN COURS///////////")
        os.chdir(r"C:\Users\Nathalie\Downloads\targetdir\2.Win_install")
        os.system("Skype-8.77.0.97.exe")
        print("///////////SKYPE INSTALLÉ///////////")

def test_zoom():
    os.chdir(r"C:\Program Files")
    if(os.path.exists(liste1[7])):
        print("///////////ZOOM EXISTE DÉJA///////////")
    else:
        print("///////////INSTALLATION ZOOM EN COURS///////////")
        os.chdir(r"C:\Users\Nathalie\Downloads\targetdir\2.Win_install")
        os.system("ZoomInstaller.exe")
        print("///////////ZOOM INSTALLÉ///////////")

def test_vlc():
    os.chdir(r"C:\Program Files (x86)")
    if(os.path.exists(liste1[8])):
        print("///////////VLC EXISTE DÉJA///////////")
    else:
        print("///////////INSTALLATION VLC EN COURS///////////")
        os.chdir(r"C:\Users\Nathalie\Downloads\targetdir\2.Win_install")
        os.system("vlc-3.0.16-win64.exe")
        print("///////////VLC INSTALLÉ///////////")

def test_java():
    os.chdir(r"C:\Program Files")
    if(os.path.exists(liste1[9])):
        print("///////////JAVA EXISTE DÉJA///////////")
    else:
        print("///////////INSTALLATION JAVA EN COURS///////////")
        os.chdir(r"C:\Users\Nathalie\Downloads\targetdir\2.Win_install")
        os.system("JavaSetup8u301.exe")
        print("///////////JAVA INSTALLÉ///////////")

def test_teams():
    os.chdir(r"C:\Users\Nathalie\AppData\Roaming")
    if(os.path.exists(liste1[10])):
        print("///////////TEAMS EXISTE DÉJA///////////")
    else:
        print("///////////INSTALLATION TEAMS EN COURS///////////")
        os.chdir(r"C:\Users\Nathalie\Downloads\targetdir\2.Win_install")
        os.system("Teams_windows_x64.exe")
        print("///////////TEAMS INSTALLÉ///////////")

def test_pdfcreator():
    os.chdir(r"C:\Program Files (x86)")
    if(os.path.exists(liste1[11])):
        print("///////////PDF_CREATOR EXISTE DÉJA///////////")
    else:
        print("///////////INSTALLATION PDF_CREATOR EN COURS///////////")
        os.chdir(r"C:\Users\Nathalie\Downloads\targetdir\2.Win_install")
        os.system("pdfcreator_26353542415234254.exe")
        print("///////////PDF_CREATOR INSTALLÉ///////////")

def test_totalav():
    os.chdir(r"C:\Program Files (x86)")
    if(os.path.exists(liste1[12])):
        print("///////////TOTAL_AV EXISTE DÉJA///////////")
    else:
        print("///////////INSTALLATION TOTAL_AV EN COURS///////////")
        os.chdir(r"C:\Users\Nathalie\Downloads\targetdir\2.Win_install")
        os.system("TotalAV_Setup.exe")
        print("///////////TOTAL_AV INSTALLÉ///////////")


print("///////////INSTALLATION DES LOGICIELS DE BASE///////////")


liste1 = ["OpenOffice 4","Filezilla","Taskcoach","Microsoft VS Code","Xampp","Adobe","Skype","Zoom",
"Vlc","Java","Teams","PdfCreator","TotalAv"]                       


#Appel de la fonction définie plus haut
test_openoffice() 
test_filezilla()
test_taskcoach()
test_vscode()
test_xampp()
test_adobe_reader()
test_skype()
test_zoom()
test_vlc()
test_java()
test_teams()
test_pdfcreator()
test_totalav()

print("///////////INSTALLATION DES LOGICIELS TERMINÉE///////////")