import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time  # Importation du module time

# Chargement des données depuis le fichier JSON
def load_data(json_path):
    with open(json_path, 'r') as file:
        return json.load(file)

# Configuration du navigateur avec options pour le téléchargement automatique du PDF
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": "C:\\Users\\a.bonjour\\Downloads",  # Chemin où vous souhaitez enregistrer le PDF
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
}
chrome_options.add_experimental_option("prefs", prefs)

# Initialisation de ChromeDriver avec le nouveau système de gestion des drivers
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://pro-siv.interieur.gouv.fr/map-ppa-ui/do/ivo_ach_redirect")

wait = 1
waitD = WebDriverWait(driver, 10)
# Attente de 30 secondes
time.sleep(30)
try:
    # Chargement des données JSON
    data = load_data('C:\\Users\\a.bonjour\\Documents\\SIV\\donnees.json')[0]  # Chargement du premier élément de la liste JSON

    # Interaction avec la page 1
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "dateDeclaration")))
    driver.find_element(By.NAME, "dateDeclaration").send_keys(data['DATE_DECLARATION'])
    time.sleep(wait)
    driver.find_element(By.NAME, "dateAchat").send_keys(data['DATE_ACHAT'])
    time.sleep(wait)
    driver.find_element(By.NAME, "heureAchat").send_keys(data['HEURE_ACHAT'])
    time.sleep(wait)
    driver.find_element(By.NAME, "numeroImmat").send_keys(data['NUMERO_IMMAT'])
    time.sleep(wait)
    driver.find_element(By.NAME, "numeroVIN").send_keys(data['NUMERO_ID'])
    time.sleep(wait)
    driver.find_element(By.ID, "valider").click()
    time.sleep(wait)

    # Interaction avec la page 2
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "idBoutonSuivant")))
    time.sleep(wait)
    driver.find_element(By.ID, "idBoutonSuivant").click()
    time.sleep(wait)

    # Interaction avec la page 3
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "agrement")))
    time.sleep(wait)
    driver.find_element(By.NAME, "agrement").send_keys("PR3700017D")
    time.sleep(wait)
    personne_morale_radio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='titulaire.isPersonnePhysique'][@value='false']"))
    )
    personne_morale_radio.click()
    time.sleep(wait)
    driver.find_element(By.NAME, "titulaire.siret").send_keys("31249335600033")
    time.sleep(wait)
    driver.find_element(By.ID, "boutonVerifierSirene").click()
    time.sleep(wait)
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.NAME, "adresseTitulaire.etage").get_attribute('value') != '')
    time.sleep(wait)
    driver.find_element(By.NAME, "adresseTitulaire.numeroVoie").send_keys("4")
    time.sleep(wait)
    driver.find_element(By.ID, "idBoutonSuivant").click()
    time.sleep(wait)

    # Interaction avec la page 4
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "certificatPourDest")))
    time.sleep(wait)
    driver.find_element(By.NAME, "certificatPourDest").click()
    time.sleep(wait)
    driver.find_element(By.NAME, "remiseJustificatifProprieteVehicule").click()
    time.sleep(wait)
    driver.find_element(By.NAME, "piecesJustificatives").click()
    time.sleep(wait)
    driver.find_element(By.ID, "valider").click()
    time.sleep(wait)

    # Interaction avec la page 5
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "idBoutonVisualiser")))
    time.sleep(wait)
    driver.find_element(By.ID, "idBoutonVisualiser").click()
    time.sleep(wait)
    # Le PDF devrait être téléchargé automatiquement dans le dossier spécifié dans les options du navigateur.
except Exception as e:
    print(f"An error occurred: {e}")
#driver.quit()
