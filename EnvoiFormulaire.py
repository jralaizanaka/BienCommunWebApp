import streamlit as st
import datetime as dt
import win32com.client
import pythoncom

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

            message = "Date: " + dateCompletDuJour + "\n" + "Nom: " + nom + "\n" + "Prénom: " + prénom + "\n" + \
                      "Date de naissance: " + ddn + "\n" + \
                      "Formation: " + formation + "\n" + "Emploi occupé: " + emploi + "\n" + \
                      "Sexe: " + sexe + "\n" + "Emploi envisagé: " + emploi_envisagé + "\n" + \
                      "Téléphone: " + numtel + "\n" + "Email: " + Email

            mailto = "j.ralaizanaka@gmail.com"

            outlook = win32com.client.Dispatch('outlook.application', pythoncom.CoInitialize())
            mail = outlook.CreateItem(0)
            mail.To = mailto
            mail.Subject = "nouveau prospect pour le bilan de compétence "
            mail.Body = message
            # mail.Display()
            mail.Send()

            st.write("Vous pouvez passez à la phase test")


if __name__ == '__main__':

    app()