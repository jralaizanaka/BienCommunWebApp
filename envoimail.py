import streamlit as st
import smtplib, ssl
import datetime as dt
import yagmail

def app():
    st.image("ImageBC.png")

    st.title("SE CONNAITRE SOIS-MEME:")

    # REMPLISSAGE DU FORMULAIRE DE CONTACT
    # -----------------------------------------------------------------

    st.subheader("Formulaire de contact 🎨")
    with st.form(key='my_form'):
        nom = st.text_input('Nom')
        prénom = st.text_input('Prénom')
        ddn = st.text_input('Date de naissance (jj/MM/AAAA)')
        formation = st.text_input('Formation')
        emploi = st.text_input('Emploi actuel')
        sexe = st.text_input('Sexe (f ou m)')
        emploi_envisagé = st.text_input('Emploi Envisagé')
        numtel = st.text_input('Numéro de téléphone')
        Email = st.text_input('Adresse Email')
        submit_button1 = st.form_submit_button(label='Envoyer')
        if submit_button1:
            dateCompletDuJour = str(dt.datetime.today().isoformat())[0:16]

            user1 = "j.ralaizanakaheroku@gmail.com"
            mypassword = "fanomezana90"
            mailto = "j.ralaizanaka@gmail.com"


            message1 = "Date: " + dateCompletDuJour + "\n" + "Nom: " + nom + "\n" + "Prenom: " + prénom + "\n" + \
                       "Date de naissance: " + ddn + "\n" + \
                       "Formation: " + formation + "\n" + "Emploi occupe: " + emploi + "\n" + \
                       "Sexe: " + sexe + "\n" + "Emploi envisage: " + emploi_envisagé + "\n" + \
                       "Telephone: " + numtel + "\n" + "Email: " + Email


            #text1 = "Nom: "+nom+ "\n"+ "Prenom: "+prénom+ "\n"+"Date de naissance:"+ddn+ "\n"
            #text2 = "Prenom: "+prénom+ "\n"
           # text3 = "Date de naissance:"+ddn+ "\n"

            yag = yagmail.SMTP(user=user1, password=mypassword)
            # sending the email
            yag.send(to=mailto, subject='Nouveau prospect', contents=message1)


