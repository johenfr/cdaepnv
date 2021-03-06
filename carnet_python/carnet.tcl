#############################################################################
# Generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#  Apr 13, 2020 06:39:30 PM CEST  platform: Linux
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set desc "-family {DejaVu Sans} -size -12"
set vTcl(actual_gui_font_text_desc) $desc
set vTcl(actual_gui_font_text_name) [font create {*}$desc]
set desc "-family {DejaVu Sans Mono} -size -12"
set vTcl(actual_gui_font_fixed_desc) $desc
set vTcl(actual_gui_font_fixed_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size -12"
set vTcl(actual_gui_font_menu_desc) $desc
set vTcl(actual_gui_font_menu_name) [font create {*}$desc]
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #111111
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) #0000ff
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top37 {base} {
    global vTcl
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu {{}} -background $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 622x732
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 1
    wm maxsize $top 1905 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Carnet d adresses"
    vTcl:DefineAlias "$top" "Carnet_d_adresses" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    ttk::style configure TNotebook -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -foreground $vTcl(actual_gui_fg)
    ttk::style configure TNotebook.Tab -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TNotebook.Tab -background [list disabled $vTcl(actual_gui_bg) selected $vTcl(pr,guicomplement_color)]
    ttk::notebook $top.tNo38 \
        -width 611 -height 733 -takefocus {} 
    vTcl:DefineAlias "$top.tNo38" "TNotebook1" vTcl:WidgetProc "Carnet_d_adresses" 1
    frame $top.tNo38.pg1 \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.tNo38.pg1" "pg1" vTcl:WidgetProc "Carnet_d_adresses" 1
    $top.tNo38 add $top.tNo38.pg1 \
        -padding 0 -sticky nsew -state normal -text Détails -image {} \
        -compound none -underline -1 
    set site_4_0  $top.tNo38.pg1
    label $site_4_0.lab40 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Nom 
    vTcl:DefineAlias "$site_4_0.lab40" "Label1" vTcl:WidgetProc "Carnet_d_adresses" 1
    label $site_4_0.cpd41 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Prénom 
    vTcl:DefineAlias "$site_4_0.cpd41" "Label2" vTcl:WidgetProc "Carnet_d_adresses" 1
    entry $site_4_0.cpd40 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black 
    vTcl:DefineAlias "$site_4_0.cpd40" "Entry7" vTcl:WidgetProc "Carnet_d_adresses" 1
    entry $site_4_0.cpd44 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black 
    vTcl:DefineAlias "$site_4_0.cpd44" "Entry2" vTcl:WidgetProc "Carnet_d_adresses" 1
    entry $site_4_0.cpd49 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black 
    vTcl:DefineAlias "$site_4_0.cpd49" "Entry3" vTcl:WidgetProc "Carnet_d_adresses" 1
    entry $site_4_0.cpd50 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black 
    vTcl:DefineAlias "$site_4_0.cpd50" "Entry4" vTcl:WidgetProc "Carnet_d_adresses" 1
    entry $site_4_0.ent37 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black 
    vTcl:DefineAlias "$site_4_0.ent37" "Entry6" vTcl:WidgetProc "Carnet_d_adresses" 1
    entry $site_4_0.cpd51 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black 
    vTcl:DefineAlias "$site_4_0.cpd51" "Entry5" vTcl:WidgetProc "Carnet_d_adresses" 1
    entry $site_4_0.ent42 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black 
    vTcl:DefineAlias "$site_4_0.ent42" "Entry1" vTcl:WidgetProc "Carnet_d_adresses" 1
    vTcl::widgets::ttk::scrolledtext::CreateCmd $site_4_0.scr42 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightcolor black -width 125 
    vTcl:DefineAlias "$site_4_0.scr42" "Entry8" vTcl:WidgetProc "Carnet_d_adresses" 1

    $site_4_0.scr42.01 configure -background white \
        -font font10 \
        -foreground black \
        -height 1 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap none
    button $site_4_0.but65 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text Enregistrer 
    vTcl:DefineAlias "$site_4_0.but65" "Button1" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_0.cpd45 \
        -takefocus {} -text Effacer 
    vTcl:DefineAlias "$site_4_0.cpd45" "TButton2" vTcl:WidgetProc "Carnet_d_adresses" 1
    label $site_4_0.cpd46 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Adresse 
    vTcl:DefineAlias "$site_4_0.cpd46" "Label3" vTcl:WidgetProc "Carnet_d_adresses" 1
    label $site_4_0.cpd47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Code postal} 
    vTcl:DefineAlias "$site_4_0.cpd47" "Label4" vTcl:WidgetProc "Carnet_d_adresses" 1
    label $site_4_0.cpd48 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Ville 
    vTcl:DefineAlias "$site_4_0.cpd48" "Label5" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_0.tBu43 \
        -takefocus {} -text Effacer 
    vTcl:DefineAlias "$site_4_0.tBu43" "TButton1" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_0.cpd52 \
        -takefocus {} -text Effacer 
    vTcl:DefineAlias "$site_4_0.cpd52" "TButton3" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_0.cpd53 \
        -takefocus {} -text Effacer 
    vTcl:DefineAlias "$site_4_0.cpd53" "TButton4" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_0.cpd54 \
        -takefocus {} -text Effacer 
    vTcl:DefineAlias "$site_4_0.cpd54" "TButton5" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::checkbutton $site_4_0.tCh58 \
        -variable tch58 -takefocus {} -text Monsieur 
    vTcl:DefineAlias "$site_4_0.tCh58" "TCheckbutton1" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::checkbutton $site_4_0.cpd59 \
        -variable tch58 -takefocus {} -text Madame 
    vTcl:DefineAlias "$site_4_0.cpd59" "TCheckbutton2" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::checkbutton $site_4_0.cpd60 \
        -variable tch58 -takefocus {} -text {Monsieur et Madame} 
    vTcl:DefineAlias "$site_4_0.cpd60" "TCheckbutton3" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::checkbutton $site_4_0.cpd61 \
        -variable tch58 -takefocus {} \
        -text {Monsieur et Madame et leurs enfants} 
    vTcl:DefineAlias "$site_4_0.cpd61" "TCheckbutton4" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_0.tBu62 \
        -takefocus {} -text Chercher 
    vTcl:DefineAlias "$site_4_0.tBu62" "TButton6" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::checkbutton $site_4_0.cpd38 \
        -variable tch58 -takefocus {} -text Mademoiselle 
    vTcl:DefineAlias "$site_4_0.cpd38" "TCheckbutton5" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::checkbutton $site_4_0.cpd39 \
        -variable tch58 -takefocus {} -text Autre 
    vTcl:DefineAlias "$site_4_0.cpd39" "TCheckbutton6" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_0.cpd63 \
        -takefocus {} -text {Tout effacer} 
    vTcl:DefineAlias "$site_4_0.cpd63" "TButton7" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_0.cpd37 \
        -takefocus {} -text Effacer 
    vTcl:DefineAlias "$site_4_0.cpd37" "TButton13" vTcl:WidgetProc "Carnet_d_adresses" 1
    label $site_4_0.cpd55 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Divers 
    vTcl:DefineAlias "$site_4_0.cpd55" "Label7" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_0.cpd68 \
        -takefocus {} -text Effacer 
    vTcl:DefineAlias "$site_4_0.cpd68" "TButton14" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TNotebook -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -foreground $vTcl(actual_gui_fg)
    ttk::style configure TNotebook.Tab -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TNotebook.Tab -background [list disabled $vTcl(actual_gui_bg) selected $vTcl(pr,guicomplement_color)]
    ttk::notebook $site_4_0.tNo57 \
        -width 442 -height 363 -takefocus {} 
    vTcl:DefineAlias "$site_4_0.tNo57" "TNotebook2" vTcl:WidgetProc "Carnet_d_adresses" 1
    frame $site_4_0.tNo57.pg1 \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_4_0.tNo57.pg1" "pg2" vTcl:WidgetProc "Carnet_d_adresses" 1
    $site_4_0.tNo57 add $site_4_0.tNo57.pg1 \
        -padding 0 -sticky nsew -state normal -text {Aperçu de l'adresse} \
        -image {} -compound none -underline -1 
    set site_6_0  $site_4_0.tNo57.pg1
    button $site_6_0.cpd69 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Imprimer 
    vTcl:DefineAlias "$site_6_0.cpd69" "Button9" vTcl:WidgetProc "Carnet_d_adresses" 1
    canvas $site_6_0.can81 \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -closeenough 1.0 \
        -height 278 -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black -width 423 
    vTcl:DefineAlias "$site_6_0.can81" "Canvas2" vTcl:WidgetProc "Carnet_d_adresses" 1
    place $site_6_0.cpd69 \
        -in $site_6_0 -x 180 -y 10 -anchor nw -bordermode inside 
    place $site_6_0.can81 \
        -in $site_6_0 -x 10 -y 50 -width 420 -height 278 -anchor nw \
        -bordermode ignore 
    frame $site_4_0.tNo57.pg0 \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_4_0.tNo57.pg0" "pg3" vTcl:WidgetProc "Carnet_d_adresses" 1
    $site_4_0.tNo57 add $site_4_0.tNo57.pg0 \
        -padding 0 -sticky nsew -state normal -text Téléphone -image {} \
        -compound none -underline -1 
    set site_6_1  $site_4_0.tNo57.pg0
    label $site_6_1.cpd70 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Nom 
    vTcl:DefineAlias "$site_6_1.cpd70" "Label17" vTcl:WidgetProc "Carnet_d_adresses" 1
    entry $site_6_1.cpd71 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black 
    vTcl:DefineAlias "$site_6_1.cpd71" "Entry17" vTcl:WidgetProc "Carnet_d_adresses" 1
    label $site_6_1.cpd72 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Numéro 
    vTcl:DefineAlias "$site_6_1.cpd72" "Label18" vTcl:WidgetProc "Carnet_d_adresses" 1
    entry $site_6_1.cpd73 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black 
    vTcl:DefineAlias "$site_6_1.cpd73" "Entry18" vTcl:WidgetProc "Carnet_d_adresses" 1
    button $site_6_1.cpd74 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Ajouter 
    vTcl:DefineAlias "$site_6_1.cpd74" "Button11" vTcl:WidgetProc "Carnet_d_adresses" 1
    button $site_6_1.cpd75 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text Supprimer 
    vTcl:DefineAlias "$site_6_1.cpd75" "Button12" vTcl:WidgetProc "Carnet_d_adresses" 1
    vTcl::widgets::ttk::scrolledtext::CreateCmd $site_6_1.cpd37 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightcolor black -width 125 
    vTcl:DefineAlias "$site_6_1.cpd37" "Text3" vTcl:WidgetProc "Carnet_d_adresses" 1

    $site_6_1.cpd37.01 configure -background white \
        -font font10 \
        -foreground black \
        -height 3 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap none
    place $site_6_1.cpd70 \
        -in $site_6_1 -x 30 -y 20 -anchor nw -bordermode inside 
    place $site_6_1.cpd71 \
        -in $site_6_1 -x 100 -y 20 -width 316 -height 20 -anchor nw \
        -bordermode inside 
    place $site_6_1.cpd72 \
        -in $site_6_1 -x 30 -y 50 -anchor nw -bordermode inside 
    place $site_6_1.cpd73 \
        -in $site_6_1 -x 100 -y 50 -width 316 -height 20 -anchor nw \
        -bordermode inside 
    place $site_6_1.cpd74 \
        -in $site_6_1 -x 30 -y 80 -anchor nw -bordermode inside 
    place $site_6_1.cpd75 \
        -in $site_6_1 -x 160 -y 80 -anchor nw -bordermode inside 
    place $site_6_1.cpd37 \
        -in $site_6_1 -x 31 -y 114 -width 386 -height 218 -anchor nw \
        -bordermode inside 
    frame $site_4_0.tNo57.pg2 \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_4_0.tNo57.pg2" "pg4" vTcl:WidgetProc "Carnet_d_adresses" 1
    $site_4_0.tNo57 add $site_4_0.tNo57.pg2 \
        -padding 0 -sticky nsew -state normal -text Courriel -image {} \
        -compound none -underline -1 
    set site_6_2  $site_4_0.tNo57.pg2
    label $site_6_2.lab36 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Adresse courriel} 
    vTcl:DefineAlias "$site_6_2.lab36" "Label6" vTcl:WidgetProc "Carnet_d_adresses" 1
    entry $site_6_2.ent37 \
        -background white -font {-family {DejaVu Sans} -size -12} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black 
    vTcl:DefineAlias "$site_6_2.ent37" "Entry9" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_6_2.tBu39 \
        -takefocus {} -text Ajouter 
    vTcl:DefineAlias "$site_6_2.tBu39" "TButton16" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_6_2.tBu40 \
        -takefocus {} -text Supprimer 
    vTcl:DefineAlias "$site_6_2.tBu40" "TButton17" vTcl:WidgetProc "Carnet_d_adresses" 1
    vTcl::widgets::ttk::scrolledtext::CreateCmd $site_6_2.scr41 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightcolor black -width 125 
    vTcl:DefineAlias "$site_6_2.scr41" "Scrolledtext1" vTcl:WidgetProc "Carnet_d_adresses" 1

    $site_6_2.scr41.01 configure -background white \
        -font font10 \
        -foreground black \
        -height 3 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap none
    place $site_6_2.lab36 \
        -in $site_6_2 -x 30 -y 20 -anchor nw -bordermode ignore 
    place $site_6_2.ent37 \
        -in $site_6_2 -x 30 -y 40 -width 386 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_6_2.tBu39 \
        -in $site_6_2 -x 30 -y 80 -anchor nw -bordermode ignore 
    place $site_6_2.tBu40 \
        -in $site_6_2 -x 130 -y 80 -anchor nw -bordermode ignore 
    place $site_6_2.scr41 \
        -in $site_6_2 -x 30 -y 110 -width 388 -height 218 -anchor nw \
        -bordermode ignore 
    vTcl::widgets::ttk::scrolledtext::CreateCmd $site_4_0.scr79 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightcolor black -width 125 
    vTcl:DefineAlias "$site_4_0.scr79" "Text1" vTcl:WidgetProc "Carnet_d_adresses" 1

    $site_4_0.scr79.01 configure -background #d9d9d9 \
        -font font10 \
        -foreground black \
        -height 3 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground red \
        -width 10 \
        -wrap word
    button $site_4_0.cpd42 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Annuler 
    vTcl:DefineAlias "$site_4_0.cpd42" "Button2" vTcl:WidgetProc "Carnet_d_adresses" 1
    button $site_4_0.cpd36 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text Supprimer 
    vTcl:DefineAlias "$site_4_0.cpd36" "Button3" vTcl:WidgetProc "Carnet_d_adresses" 1
    place $site_4_0.lab40 \
        -in $site_4_0 -x 20 -y 60 -anchor nw -bordermode ignore 
    place $site_4_0.cpd41 \
        -in $site_4_0 -x 20 -y 90 -anchor nw -bordermode inside 
    place $site_4_0.cpd40 \
        -in $site_4_0 -x 0 -relx 0.516 -y 0 -rely 0.042 -width 196 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode inside 
    place $site_4_0.cpd44 \
        -in $site_4_0 -x 0 -relx 0.177 -y 0 -rely 0.085 -width 406 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode inside 
    place $site_4_0.cpd49 \
        -in $site_4_0 -x 0 -relx 0.177 -y 0 -rely 0.127 -width 406 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode inside 
    place $site_4_0.cpd50 \
        -in $site_4_0 -x 0 -relx 0.177 -y 0 -rely 0.17 -width 406 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode inside 
    place $site_4_0.ent37 \
        -in $site_4_0 -x 0 -relx 0.177 -y 0 -rely 0.198 -width 406 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.cpd51 \
        -in $site_4_0 -x 0 -relx 0.177 -y 0 -rely 0.24 -width 406 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode inside 
    place $site_4_0.ent42 \
        -in $site_4_0 -x 0 -relx 0.177 -y 0 -rely 0.283 -width 406 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.scr42 \
        -in $site_4_0 -x 0 -relx 0.177 -y 0 -rely 0.325 -width 0 \
        -relwidth 0.655 -height 0 -relheight 0.096 -anchor nw \
        -bordermode ignore 
    place $site_4_0.but65 \
        -in $site_4_0 -x 380 -y 300 -anchor nw -bordermode ignore 
    place $site_4_0.cpd45 \
        -in $site_4_0 -x 0 -relx 0.847 -y 0 -rely 0.078 -anchor nw \
        -bordermode inside 
    place $site_4_0.cpd46 \
        -in $site_4_0 -x 20 -y 120 -anchor nw -bordermode inside 
    place $site_4_0.cpd47 \
        -in $site_4_0 -x 20 -y 170 -anchor nw -bordermode inside 
    place $site_4_0.cpd48 \
        -in $site_4_0 -x 20 -y 200 -anchor nw -bordermode inside 
    place $site_4_0.tBu43 \
        -in $site_4_0 -x 0 -relx 0.847 -y 0 -rely 0.276 -anchor nw \
        -bordermode ignore 
    place $site_4_0.cpd52 \
        -in $site_4_0 -x 0 -relx 0.847 -y 0 -rely 0.12 -anchor nw \
        -bordermode inside 
    place $site_4_0.cpd53 \
        -in $site_4_0 -x 0 -relx 0.847 -y 0 -rely 0.184 -width 83 -height 25 \
        -anchor nw -bordermode ignore 
    place $site_4_0.cpd54 \
        -in $site_4_0 -x 0 -relx 0.847 -y 0 -rely 0.233 -anchor nw \
        -bordermode inside 
    place $site_4_0.tCh58 \
        -in $site_4_0 -x 20 -y 10 -anchor nw -bordermode ignore 
    place $site_4_0.cpd59 \
        -in $site_4_0 -x 20 -y 30 -anchor nw -bordermode inside 
    place $site_4_0.cpd60 \
        -in $site_4_0 -x 100 -y 10 -anchor nw -bordermode inside 
    place $site_4_0.cpd61 \
        -in $site_4_0 -x 0 -relx 0.419 -y 0 -rely 0.014 -width 0 \
        -relwidth 0.423 -height 0 -relheight 0.03 -anchor nw \
        -bordermode inside 
    place $site_4_0.tBu62 \
        -in $site_4_0 -x 20 -y 300 -anchor nw -bordermode ignore 
    place $site_4_0.cpd38 \
        -in $site_4_0 -x 0 -relx 0.161 -y 0 -rely 0.042 -width 0 \
        -relwidth 0.194 -height 0 -relheight 0.025 -anchor nw \
        -bordermode inside 
    place $site_4_0.cpd39 \
        -in $site_4_0 -x 0 -relx 0.419 -y 0 -rely 0.042 -width 0 \
        -relwidth 0.092 -height 0 -relheight 0.03 -anchor nw \
        -bordermode inside 
    place $site_4_0.cpd63 \
        -in $site_4_0 -x 0 -relx 0.831 -y 0 -rely 0.424 -anchor nw \
        -bordermode inside 
    place $site_4_0.cpd37 \
        -in $site_4_0 -x 0 -relx 0.847 -y 0 -rely 0.028 -anchor nw \
        -bordermode inside 
    place $site_4_0.cpd55 \
        -in $site_4_0 -x 20 -y 230 -anchor nw -bordermode inside 
    place $site_4_0.cpd68 \
        -in $site_4_0 -x 0 -relx 0.847 -y 0 -rely 0.354 -anchor nw \
        -bordermode inside 
    place $site_4_0.tNo57 \
        -in $site_4_0 -x 0 -relx 0.25 -y 0 -rely 0.467 -width 0 \
        -relwidth 0.737 -height 0 -relheight 0.513 -anchor nw \
        -bordermode ignore 
    place $site_4_0.scr79 \
        -in $site_4_0 -x 20 -y 330 -width 126 -height 358 -anchor nw \
        -bordermode ignore 
    place $site_4_0.cpd42 \
        -in $site_4_0 -x 290 -y 300 -anchor nw -bordermode inside 
    place $site_4_0.cpd36 \
        -in $site_4_0 -x 200 -y 300 -width 73 -height 26 -anchor nw \
        -bordermode inside 
    frame $top.tNo38.pg0 \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.tNo38.pg0" "pg0" vTcl:WidgetProc "Carnet_d_adresses" 1
    $top.tNo38 add $top.tNo38.pg0 \
        -padding 0 -sticky nsew -state normal -text Liste -image {} \
        -compound none -underline -1 
    set site_4_1  $top.tNo38.pg0
    labelframe $site_4_1.lab70 \
        -font TkDefaultFont -foreground black -text {Carnet d'adresses} \
        -background $vTcl(actual_gui_bg) -height 155 -highlightcolor black \
        -width 575 
    vTcl:DefineAlias "$site_4_1.lab70" "Labelframe1" vTcl:WidgetProc "Carnet_d_adresses" 1
    set site_5_0 $site_4_1.lab70
    ttk::combobox $site_5_0.tCo37 \
        -font TkTextFont -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$site_5_0.tCo37" "TCombobox1" vTcl:WidgetProc "Carnet_d_adresses" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $site_5_0.scr39 \
        -background $vTcl(actual_gui_bg) -height 75 -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$site_5_0.scr39" "Scrolledlistbox1" vTcl:WidgetProc "Carnet_d_adresses" 1

    $site_5_0.scr39.01 configure -background white \
        -cursor xterm \
        -font TkFixedFont \
        -foreground black \
        -height 7 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 78
    place $site_5_0.tCo37 \
        -in $site_5_0 -x 10 -y 14 -width 177 -height 18 -anchor nw \
        -bordermode ignore 
    place $site_5_0.scr39 \
        -in $site_5_0 -x 10 -y 34 -width 552 -height 109 -anchor nw \
        -bordermode ignore 
    labelframe $site_4_1.cpd71 \
        -font TkDefaultFont -foreground black -text {Liste sélectionnée} \
        -background $vTcl(actual_gui_bg) -height 165 -highlightcolor black \
        -width 575 
    vTcl:DefineAlias "$site_4_1.cpd71" "Labelframe2" vTcl:WidgetProc "Carnet_d_adresses" 1
    set site_5_0 $site_4_1.cpd71
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $site_5_0.scr46 \
        -background $vTcl(actual_gui_bg) -height 75 -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$site_5_0.scr46" "Scrolledlistbox2" vTcl:WidgetProc "Carnet_d_adresses" 1

    $site_5_0.scr46.01 configure -background white \
        -cursor xterm \
        -font TkFixedFont \
        -foreground black \
        -height 13 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 78
    place $site_5_0.scr46 \
        -in $site_5_0 -x 10 -y 14 -width 552 -height 139 -anchor nw \
        -bordermode ignore 
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_1.tBu72 \
        -takefocus {} -text Ajouter 
    vTcl:DefineAlias "$site_4_1.tBu72" "TButton8" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_1.cpd73 \
        -takefocus {} -text Enlever 
    vTcl:DefineAlias "$site_4_1.cpd73" "TButton9" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_1.tBu74 \
        -takefocus {} -text {Imprimer l'aperçu} 
    vTcl:DefineAlias "$site_4_1.tBu74" "TButton10" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_1.cpd75 \
        -takefocus {} -text {Imprimer la liste sélectionnée} 
    vTcl:DefineAlias "$site_4_1.cpd75" "TButton11" vTcl:WidgetProc "Carnet_d_adresses" 1
    label $site_4_1.cpd80 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Aperçu de l'impression} 
    vTcl:DefineAlias "$site_4_1.cpd80" "Label10" vTcl:WidgetProc "Carnet_d_adresses" 1
    canvas $site_4_1.can84 \
        -background $vTcl(actual_gui_bg) -closeenough 1.0 -height 278 \
        -highlightcolor black -insertbackground black \
        -selectbackground #d9d9d9 -selectforeground black -width 420 
    vTcl:DefineAlias "$site_4_1.can84" "Canvas1" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_1.cpd37 \
        -takefocus {} -text {Tout ajouter} 
    vTcl:DefineAlias "$site_4_1.cpd37" "TButton12" vTcl:WidgetProc "Carnet_d_adresses" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_1.cpd38 \
        -takefocus {} -text {Tout enlever} 
    vTcl:DefineAlias "$site_4_1.cpd38" "TButton15" vTcl:WidgetProc "Carnet_d_adresses" 1
    place $site_4_1.lab70 \
        -in $site_4_1 -x 10 -y 0 -width 575 -height 155 -anchor nw \
        -bordermode ignore 
    place $site_4_1.cpd71 \
        -in $site_4_1 -x 10 -y 190 -width 575 -height 165 -anchor nw \
        -bordermode inside 
    place $site_4_1.tBu72 \
        -in $site_4_1 -x 190 -y 160 -width 73 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_4_1.cpd73 \
        -in $site_4_1 -x 280 -y 160 -width 73 -height 25 -anchor nw \
        -bordermode inside 
    place $site_4_1.tBu74 \
        -in $site_4_1 -x 190 -y 360 -anchor nw -bordermode ignore 
    place $site_4_1.cpd75 \
        -in $site_4_1 -x 350 -y 360 -anchor nw -bordermode inside 
    place $site_4_1.cpd80 \
        -in $site_4_1 -x 20 -y 370 -anchor nw -bordermode inside 
    place $site_4_1.can84 \
        -in $site_4_1 -x 70 -y 410 -width 420 -relwidth 0 -height 278 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_1.cpd37 \
        -in $site_4_1 -x 90 -y 160 -anchor nw -bordermode inside 
    place $site_4_1.cpd38 \
        -in $site_4_1 -x 370 -y 160 -anchor nw -bordermode inside 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tNo38 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1.002 -height 0 \
        -relheight 1.001 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top37 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

