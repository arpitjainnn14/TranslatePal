import streamlit as st

import asyncio
from googletrans import Translator

st.title("Basic Translation")


async def main():
    translator = Translator()
    
    try:
        text = st.text_input("Enter the text to translate",value=" ")
        dest_lan = st.text_input("Enter the destination language (e.g. 'fr' for French): ")
        
        result = await translator.translate(text, dest=dest_lan, src='auto')
        answer=st.write(f"Resulted text:\n{result.text}")
        return answer
    except Exception as e:
        st.write("Write the text and Destination to start the Translator app")
# Run the asynchronous function
asyncio.run(main())
