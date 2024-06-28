import socket
import threading
import tkinter
from tkinter import simpledialog

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

class ChatGUI:
       def __init__(self):
              self.root =tkinter.Tk()
              self.root.title('Chat APP!')

              self.chat_label = tkinter.Label(self.root, text='Chat: ')
              self.chat_label.pack(padx=20, pady=20)

              self.text_area = tkinter.Text(self.root)
              self.text_area.pack(padx=20, pady=20)
              self.text_area.config(state='disabled')

              self.msg_label = tkinter.Label(self.root, text='Message:')
              self.msg_label.pack(padx=20, pady=20)

              self.input_area = tkinter.Text(self.root, height=3)
              self.input_area.pack(padx=20, pady=5)

              self.send_button = tkinter.Button(self.root, text='Send', command=self.write)
              self.send_button.pack(padx=20, pady=5)

              self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

              self.nickname = simpledialog.askstring('Nickname', 'Please Choose a nickname', parent=self.root)

              self.receive_thread = threading.Thread(target=self.receive)
              self.receive_thread.start()

              self.root.mainloop()

       def write(self):
              message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
              client.send(message.encode('utf-8'))
              self.input_area.delete('1.0','end')

       def receive(self):
              while True:
                     try:
                            message = client.recv(1024).decode('utf-8')
                            self.text_area.config(state='normal')
                            self.text_area.insert('end', message)
                            self.text_area.yview('end')
                            self.text_area.config(state='disabled')
                     
                     except ConnectionAbortedError:
                            break
                     except:
                            print('An Error occured!')
                            client.close()
                            break

       def on_closing(self):
              client.close()
              self.root.destroy()

chat_gui = ChatGUI()

                     