import tkinter as tk
# import time


# def update_clock():
#        currrent_time = time.strftime('%H: %M: %S')
#        clock_label.config(text = currrent_time)
#        root.after(1000, update_clock)

# root = tk.Tk()
# root.title('Clock')

# clock_label = tk.Label(root, font=('Arial', 18))
# clock_label.pack()

# update_clock()
# root.mainloop()

import datetime

def scheduled_time():
       now = datetime.datetime.now()
       if now.hour == 12 and now.minute == 0:
              reminder_label.config(text='Waktunya minum obat!')
       else:
              reminder_label.config(text='')
       root.after(60000, scheduled_time)

root = tk.Tk()
root.title('Reminder')

reminder_label = tk.Label(root, font=('Arial', 18))
reminder_label.pack()

scheduled_time()
root.mainloop()
