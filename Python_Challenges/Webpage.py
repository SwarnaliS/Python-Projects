import webbrowser


def my_page():
    f = open ('my.html', 'w')
    f.write("""<html>
        <body>
            <h2>
                Stay Tuned for our amazing summer sale!
            </h2>

        </body>
    </html>""" )
    f.close()
webbrowser.open_new_tab("C:/Users/Swarnali/Desktop/Tech_Academy_Github/Python-Projects/Python_Challenges/my.html")


