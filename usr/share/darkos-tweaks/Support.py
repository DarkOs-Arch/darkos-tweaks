import gi
import Functions
from Functions import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

base_dir = os.path.dirname(os.path.realpath(__file__))


class Support(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Credits - Support Development", parent, 0)
        # self.add_buttons(Gtk.STOCK_OK,Gtk.ResponseType.OK)
        
        self.set_size_request(550, 100)
        # self.set_resizable(False)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        box = self.get_content_area()
        box.pack_start(vbox, False, False, 0)
        
        label = Gtk.Label()
        label3 = Gtk.Label()
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.CENTER)
        label.set_markup("This Tool Was Developed by <b>Brad Heffernan</b> And The Help Of <b>Krisztian Veress</b> And <b>Erik Dubois</b>\n\
And It Was Edited For DarkOs By <b>Ybenel</b> If You Want To Support The Developers For Their Hard Work You Can Do So By Using Listed Methods Bellow.")
        label2 = Gtk.Label()
        label2.set_markup("Support <b>Devs</b> Through")
        # =====================================================
        #               PATREON LINK
        # =====================================================
        pE = Gtk.EventBox()
        ppE = Gtk.EventBox()
        erik = Gtk.EventBox()

        erik_yt = GdkPixbuf.Pixbuf().new_from_file_at_size(os.path.join(base_dir, 'images/erik_yt.png'),100,100)
        erik_load = Gtk.Image().new_from_pixbuf(erik_yt)

        pbp = GdkPixbuf.Pixbuf().new_from_file_at_size(
            os.path.join(base_dir, 'images/patreon.png'), 48, 48)
        pimage = Gtk.Image().new_from_pixbuf(pbp)

        logo = GdkPixbuf.Pixbuf().new_from_file_at_size(
            os.path.join(base_dir, 'images/darkos-bright.png'), 100, 100)
        logo_image = Gtk.Image().new_from_pixbuf(logo)

        erik.add(erik_load)
        erik.connect("button_press_event", self.on_support_click, "https://www.youtube.com/user/maclover696")
        erik.set_property("has-tooltip",True)
        erik.connect('query-tooltip',self.tooltip_callback,"Subscribe To Erik On Youtube")

        pE.add(pimage)

        pE.connect("button_press_event", self.on_support_click, "https://www.patreon.com/hefftor")
        pE.set_property("has-tooltip", True)

        pE.connect("query-tooltip", self.tooltip_callback, "Support BradHeff on Patreon")

        

        pbpp = GdkPixbuf.Pixbuf().new_from_file_at_size(
            os.path.join(base_dir, 'images/paypal.png'), 54, 54)
        ppimage = Gtk.Image().new_from_pixbuf(pbpp)

        ppE.add(ppimage)

        ppE.connect("button_press_event", self.on_support_click, "https://PayPal.Me/heffserver")
        ppE.set_property("has-tooltip", True)

        ppE.connect("query-tooltip", self.tooltip_callback, "Buy BradHeff a coffee")

        pE_label = Gtk.Label("Patreon")
        
        vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        hbox.pack_start(label, True, True, 10)

        hbox1.pack_start(label2, False, False, 10)
        
        vbox1.pack_start(pE, False, False, 0)
        vbox1.pack_start(pE_label, False, False, 0)

        hbox2.pack_start(vbox1, False, False, 10)
        hbox2.pack_start(ppE, False, False, 10)
        hbox2.pack_start(erik,False,False,10)
        hbox3.pack_start(hbox2, True, False, 0)

        # hbox4.pack_start(erik,False,False,10)

        vbox.pack_start(logo_image, False, False, 10)
        vbox.pack_start(hbox, False, False, 10)
        
        vbox.pack_end(hbox3, False, False, 10)
        vbox.pack_end(hbox1, False, False, 0)
        # vbox.pack_end(hbox4, False, False, 0)
        
        self.show_all()

    def on_support_click(self, widget, event, link):
        t = Functions.threading.Thread(target=self.weblink, args=(link,))
        t.daemon = True
        t.start()
        # print("CLICKED")
        # self.weblink(link)

    def weblink(self, link):
        Functions.subprocess.call(["sudo", "-H", "-u", Functions.sudo_username, "bash", "-c", "exo-open --launch webbrowser " + link], shell=False)
        # webbrowser.open_new_tab(link)

    def tooltip_callback(self, widget, x, y, keyboard_mode, tooltip, text):
        tooltip.set_text(text)
        return True
