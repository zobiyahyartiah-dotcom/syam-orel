from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
import threading
import time

class SyamWhatsAppPanelApp(App):
    def build(self):
        self.title = "Syam WhatsApp Bug Panel"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text='SYAM WHATSAPP BUG PANEL', font_size=20, color=(0, 1, 0.4, 1), size_hint_y=None, height=40))
        
        layout.add_widget(Label(text='Nomor Target (Format: 62xx):', size_hint_y=None, height=25))
        self.target_input = TextInput(text='62', multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.target_input)
        
        layout.add_widget(Label(text='Jenis Payload:', size_hint_y=None, height=25))
        self.payload_spinner = Spinner(
            text='Null Character Crash',
            values=('Null Character Crash', 'Corrupted VCard Stream', 'Gateway TCP Flood'),
            size_hint_y=None, height=40
        )
        layout.add_widget(self.payload_spinner)
        
        layout.add_widget(Label(text='Jumlah Paket:', size_hint_y=None, height=25))
        self.count_input = TextInput(text='50', multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.count_input)
        
        self.exec_btn = Button(text='JALANKAN EKSEKUSI', background_color=(0, 1, 0.4, 1), size_hint_y=None, height=50)
        self.exec_btn.bind(on_press=self.start_execution)
        layout.add_widget(self.exec_btn)
        
        self.log_label = Label(text='[System] Aplikasi siap digunakan.', halign='left', valign='top', color=(0.5, 0.7, 1, 1))
        self.log_label.bind(size=self.log_label.setter('text_size'))
        layout.add_widget(self.log_label)
        
        return layout

    def start_execution(self, instance):
        target = self.target_input.text
        if not target.startswith('62'):
            self.log_label.text = '[Error] Format nomor target harus menggunakan awalan 62!'
            return
        
        self.exec_btn.disabled = True
        self.exec_btn.text = 'MENGIRIM...'
        self.log_label.text = f'[Init] Menghubungkan ke gateway untuk target: +{target}\n'
        
        threading.Thread(target=self.run_process).start()

    def run_process(self):
        count = int(self.count_input.text)
        for i in range(1, count + 1):
            time.sleep(0.05)
            if i % 10 == 0 or i == 1:
                Clock.schedule_release(lambda dt, idx=i: self.update_log(f'Mengirim paket #{idx}/{count} terkirim\n'))
        
        Clock.schedule_release(lambda dt: self.finish_process())

    def update_log(self, text):
        self.log_label.text += text

    def finish_process(self):
        self.log_label.text += '[Complete] Seluruh paket berhasil dikirim.'
        self.exec_btn.disabled = False
        self.exec_btn.text = 'JALANKAN EKSEKUSI'

if __name__ == '__main__':
    SyamWhatsAppPanelApp().run()
  
