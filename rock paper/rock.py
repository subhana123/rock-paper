import streamlit as st
import random

def main():
    st.set_page_config(page_title="Rock, Paper, Scissors", page_icon="✊✋✌️")
    st.title("✊✋✌️ Rock, Paper, Scissors Game")

    choices = ['Rock', 'Paper', 'Scissors']
    user_choice = st.selectbox("Choose your move:", choices)

    if st.button("Play!"):
        computer_choice = random.choice(choices)
        st.write(f"🤖 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            st.info("It's a draw! 🤝")
        elif (
            (user_choice == 'Rock' and computer_choice == 'Scissors') or
            (user_choice == 'Paper' and computer_choice == 'Rock') or
            (user_choice == 'Scissors' and computer_choice == 'Paper')
        ):
            st.success("You win! 🎉")
        else:
            st.error("You lose! 😢")


if __name__ == "__main__":
    main()
