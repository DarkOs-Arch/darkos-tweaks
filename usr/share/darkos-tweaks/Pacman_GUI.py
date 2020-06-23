# =================================================================
# =                  Author: Brad Heffernan      
# =                  Edited By: Ybenel   
# =================================================================

# import pacman_functions


def GUI(self, Gtk, vboxStack1, Functions):
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    lbl1 = Gtk.Label(xalign=0)
    lbl1.set_text("Pacman Config Editor")
    lbl1.set_name("title")
    hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    hbox4.pack_start(hseparator, True, True, 0)
    hbox3.pack_start(lbl1, False, False, 0)
    # ==========================================================
    #                   GLOBALS
    # ==========================================================
    hboxStack2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    hboxStack8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

    # ========================================================
    #               DarkOs REPOS
    # ========================================================
    frame3 = Gtk.Frame(label="")
    frame3lbl = frame3.get_label_widget()
    frame3lbl.set_markup("<b>DarkOs repos</b>")
    
    self.dark_repo_button = Gtk.Switch()
    self.dark_repo_button.connect("notify::active", self.on_pacman_dark_repo_toggle)
    label6 = Gtk.Label(xalign=0)
    label6.set_markup("Enable DarkOs repo")




    # ========================================================
    #               ARCHLINUX REPOS
    # ========================================================
    frame = Gtk.Frame(label="")
    framelbl = frame.get_label_widget()
    framelbl.set_markup("<b>Arch Linux repos</b>")

    self.checkbutton2 = Gtk.Switch()
    self.checkbutton2.connect("notify::active", self.on_pacman_toggle2)
    label3 = Gtk.Label(xalign=0)
    label3.set_markup("Enable Arch Linux test repo")

    self.checkbutton3 = Gtk.Switch()
    self.checkbutton3.connect("notify::active", self.on_pacman_toggle3)
    label4 = Gtk.Label(xalign=0)
    label4.set_markup("Enable Arch Linux multilib test repo")

    self.checkbutton4 = Gtk.Switch()
    self.checkbutton4.connect("notify::active", self.on_pacman_toggle4)
    label10 = Gtk.Label(xalign=0)
    label10.set_markup("Enable Arch Linux community test repo")

    # ========================================================
    #               ArcoLinux REPOS
    # ========================================================

    frame2 = Gtk.Frame(label="")
    frame2lbl = frame2.get_label_widget()
    frame2lbl.set_markup("<b>ArcoLinux repos</b>")

    self.arepo_button = Gtk.Switch()
    self.arepo_button.connect("notify::active", self.on_pacman_arepo_toggle)
    label5 = Gtk.Label(xalign=0)
    label5.set_markup("Enable ArcoLinux repo")


    # ========================================================
    #               CUSTOM REPOS
    # ========================================================
    label2 = Gtk.Label(xalign=0)
    label2.set_markup("<b>Add custom repo to pacman.conf</b>")

    self.textbox1 = Gtk.TextView()
    self.textbox1.set_wrap_mode(Gtk.WrapMode.WORD)
    self.textbox1.set_editable(True)
    self.textbox1.set_cursor_visible(True)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.LEFT, 1)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.RIGHT, 1)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.TOP, 1)
    self.textbox1.set_border_window_size(Gtk.TextWindowType.BOTTOM, 1)

    sw = Gtk.ScrolledWindow()
    sw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
    sw.add(self.textbox1)

    # ========================================================
    #               FOOTER
    # ========================================================
    self.button1 = Gtk.Button(label="Apply custom repo")
    self.button1.connect('clicked', self.button1_clicked)
    reset_pacman = Gtk.Button(label="Reset pacman")
    reset_pacman.connect("clicked", self.reset_settings, Functions.pacman)

    # ========================================================
    #               DarkOs REPOS PACKING
    # ========================================================
    hboxStack8.pack_start(label6, False, True, 10)
    hboxStack8.pack_end(self.dark_repo_button, False, False, 10)

    # ========================================================
    #               ArcoLinux REPOS PACKING
    # ========================================================
    hboxStack7.pack_start(label5, False, True, 10)
    hboxStack7.pack_end(self.arepo_button, False, False, 10)
    vboxStack4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    vboxStack4.pack_start(hboxStack7, False, False, 10)
   

    # ========================================================
    #               TESTING REPOS PACKING
    # ========================================================
    hboxStack5.pack_start(label3, False, True, 10)
    hboxStack5.pack_end(self.checkbutton2, False, False, 10)
    hboxStack6.pack_start(label4, False, True, 10)
    hboxStack6.pack_end(self.checkbutton3, False, False, 10)
    hboxStack12.pack_start(label10, False, True, 10)
    hboxStack12.pack_end(self.checkbutton4, False, False, 10)

    vboxStack3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    vboxStack3.pack_start(hboxStack6, False, False, 10)
    # ========================================================
    #               CUSTOM REPOS PACKING
    # ========================================================
    hboxStack2.pack_start(label2, False, True, 10)
    hboxStack3.pack_start(sw, True, True, 10)

    # ========================================================
    #               BUTTONS PACKING
    # ========================================================
    hboxStack4.pack_end(self.button1, False, False, 0)
    hboxStack4.pack_end(reset_pacman, False, False, 0)

    # ========================================================
    #               TESTING REPOS PACKING TO FRAME
    # ========================================================
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    vbox.pack_start(hboxStack5, False, False, 10)
    vbox.pack_start(hboxStack12, False, False, 0)
    vbox.pack_start(vboxStack3, False, False, 0)
    frame.add(vbox)
    
    # ========================================================
    #               DarkOs REPOS PACKING TO FRAME
    # ========================================================
    vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    vbox3.pack_start(hboxStack8, False, False, 0)
    frame3.add(vbox3)
    
    # ========================================================
    #               ArcoLinux REPOS PACKING TO FRAME
    # ========================================================
    vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    vbox2.pack_start(vboxStack4, False, False, 0)
    frame2.add(vbox2)

    # ========================================================
    #               PACK TO WINDOW
    # ========================================================
    # =================ARCO REPO========================
    vboxStack1.pack_start(hbox3, False, False, 5)
    vboxStack1.pack_start(hbox4, False, False, 5)
    vboxStack1.pack_start(frame3, False, False, 5)
    # frame4.add(hboxStack1)
    # =================TESTING REPO========================
    vboxStack1.pack_start(frame, False, False, 5)

    # =================SPINOFF REPO========================
    vboxStack1.pack_start(frame2, False, False, 0)

    # =================CUSTOM REPO========================
    vboxStack1.pack_start(hboxStack2, False, False, 0)
    vboxStack1.pack_start(hboxStack3, True, True, 0)

    # =================FOOTER========================
    vboxStack1.pack_end(hboxStack4, False, False, 0)