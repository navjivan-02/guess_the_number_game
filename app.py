import streamlit as st
import random

# Initialize session state variables
if 'computer_number' not in st.session_state:
    st.session_state.computer_number = random.randint(1, 100)
    st.session_state.guess_count = 0
    st.session_state.game_over = False

st.title("🎯 The Perfect Guess")
st.subheader("Guess the number I'm thinking of between 1 and 100!")

# Input for user's guess
if not st.session_state.game_over:
    user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Guess"):
        st.session_state.guess_count += 1

        if user_guess == st.session_state.computer_number:
            st.success(f"🥳 You guessed it right in {st.session_state.guess_count} tries!")
            st.balloons()
            st.session_state.game_over = True
        elif user_guess < st.session_state.computer_number:
            st.info("🔼 Try a higher number!")
        else:
            st.info("🔽 Try a lower number!")

# Restart game
if st.button("Restart Game"):
    st.session_state.computer_number = random.randint(1, 100)
    st.session_state.guess_count = 0
    st.session_state.game_over = False
    st.experimental_rerun()
