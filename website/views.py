from flask import (
    Blueprint, render_template, url_for
)

views = Blueprint('views', __name__)


@views.route('/')
@views.route('/base.html')
def home():
    return render_template("base.html", title="Keyboard Part Picker")


@views.route('/bulidGuide.html')
def bulid_guide():
    pcb = '''
    The PCB is the most important part of the keyboard. It is what gives the keyboard life. When trying to come up with a build,
                   'there are centain sizes of PCB that we recommend to stick to, '
                   ' 60 % , 75%, 80 % , 90%, and 100%. The reason for this is that these sizes have the most support and components on '
                   'the market right now. In addition to thinking about the size of the PCB, you must think about the '
                   'type of PCB you want for your build. For the beginner level, we suggest a Hot-Swappable PCB as there '
                   ' is no soldering at all. If you fancy yourself handy with electronics then you can either go for a '
                   'Standard PCB or a Through-hole PCB. The Standard only requires you to solder the switches and the '
                   'Through-hole requires you to solder everything from diodes to the USB connector.'
                   'paragraph = for r in paragraph
                   '''
    case = '''
        The Case is what holds all of the components and is one of the main factors that contributes the the
        sound generated from a keyboard. Cases come in many type of material such as plastic, wood, carbon
        fiber, aluminium, etc.'''

    plate = '''
        The Plate is the main part of the keyboard. It is what gives the keyboard life. When trying to come up with a build,
    '''

    stabilizers = '''             
      The PCB is the most important part of the keyboard. It is what gives the keyboard life. When trying
      to come up with a build, there are centain sizes of PCB that we reccomend to stick to, 60%, 75%,
      80%, 90%, and 100%. The for this is that these sizes have the most support and components on the
      market right now.
      '''

    switches = '''
    The PCB is the most important part of the keyboard. It is what gives the keyboard life. When trying
     to come up with a build, there are centain sizes of PCB that we reccomend to stick to, 60%, 75%,
                    80%, 90%, and 100%. The for this is that these sizes have the most support and components on the
                    market right now.
    '''

    keycaps = ''' 
        The PCB is the most important part of the keyboard. It is what gives the keyboard life. When trying
        to come up with a build, there are centain sizes of PCB that we reccomend to stick to, 60%, 75%,
        80%, 90%, and 100%. The for this is that these sizes have the most support and components on the
        market right now.
    '''

    images = ['img/pcb.jpeg', 'img/case.jpeg', 'img/plate.jpeg',
              'img/stabs.jpeg', 'img/switches.jpeg', 'img/kcps.jpeg']
    paragraph = [pcb, case, plate, stabilizers, switches, keycaps]
    return render_template("bulidGuide.html", title="Build Guide", paragraph=paragraph, images=images)


@views.route('/inspiration.html')
def inspiration():
    return render_template("inspiration.html", title="Inspiration",)


@views.route('/bulidPage.html')
def bulid_page():
    return render_template("bulidPage.html", title="Build Page",)


@views.route('/teamMem.html')
def team_member():
    return render_template("teamMem.html", title="Team Member Page",)


@views.route('partsSelection/pcb.html')
def pcb():
    return render_template("partsSelection/pcb.html", title="PCB Page",)


@views.route('partsSelection/case.html')
def case():
    return render_template("partsSelection/case.html", title="Case Page",)


@views.route('partsSelection/plate.html')
def plate():
    return render_template("partsSelection/plate.html", title="Plate Page",)


@views.route('partsSelection/stabilizers.html')
def stabilizers():
    return render_template("partsSelection/stabilizers.html", title="Stabilizers Page",)


@views.route('partsSelection/switches.html')
def switches():
    return render_template("partsSelection/switches.html", title="Switches Page",)


@views.route('partsSelection/keycaps.html')
def keycaps():
    return render_template("partsSelection/keycaps.html", title="Keycaps Page",)
