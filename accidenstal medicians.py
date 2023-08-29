< !doctype
html >
{ % load
static %}
< html
lang = "en" >
< head >
< !-- Required
meta
tags -->
< meta
charset = "utf-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1, shrink-to-fit=no" >
< link
rel = "shortcut icon"
href = "{% static 'IMAGES/favicon.ico' %}"
type = "image/x-icon" >
< link
rel = "icon"
href = "{% static 'IMAGES/favicon.ico' %}"
type = "image/x-icon" >
< !-- Bootstrap
CSS -->
< link
rel = "stylesheet"
href = "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
integrity = "sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
crossorigin = "anonymous" >
< link
rel = "stylesheet"
href = "{% static '/CSS/accident_n_emergencies.css' %}" >
< title > Accidents and Emergencies < / title >
< / head >
< body >
< nav


class ="navbar navbar-expand-lg navbar-light" >

< div


class ="container-fluid" >

< a


class ="navbar-brand" href="#" > MITIAN's DOCTOR</a>

< button


class ="navbar-toggler"


type = "button"
data - bs - toggle = "collapse"
data - bs - target = "#navbarSupportedContent"
aria - controls = "navbarSupportedContent"
aria - expanded = "false"
aria - label = "Toggle navigation"
>
< span


class ="navbar-toggler-icon" > < / span >

< / button >
< div


class ="collapse navbar-collapse" id="navbarSupportedContent" >

< ul


class ="navbar-nav me-auto mb-2 mb-lg-0" >

< li


class ="nav-item" >

< a


class ="nav-link active"


aria - current = "page"
href = "{% url 'home' %}"
> Home < / a
>
< / li >
< li


class ="nav-item" >

< a


class ="nav-link" href="{% url 'about' %}" > About < / a >

< / li >

< li


class ="nav-item" >

< a


class ="nav-link" href="{% url 'contact_us' %}" > Contact Us < / a >

< / li >

< / ul >
< / div >
< / div >
< / nav >
< hr >
< main >
< div


class ="div1" >

< img
src = "{% static '/IMAGES/artificial respiration.jpg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Artificial
Respiration < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal1" >


Check
< / button >
< div


class ="modal fade" id="modal1" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Artificial Respiration < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Administration
of
artificial
respiration is one
of
the
crucial
aspects
of
first
aid.The
mouth - to - mouth and mouth - to - nose
methods
described
here
are
simple
enough
to
be
mastered
by
anyone
who
takes
the
trouble
to
practice
them
before
emergency
necessitates
their
use.They
are
also
considered
by
authorities
more
effective
than
other
techniques. < / p >
< p > < b > Mouth
to
Mouth
Resuscitation: < / b > < / p >
< hr >
< p > < b > What
to
do: < / b > < / p >
< p > 1.
Stretch
out
victim
on
his
back and kneel
close
to
his
side.Loosen
any
tight
clothing
around
his
neck or chest. < / p >
< p > 2.
Remove
foreign
objects if present
from victim

's mouth and throat by finger sweeping. If the patient seems to have water or mucus in his throat or chest, tilt him upside down or on his side to permit such fluid to run out the mouth. </p>
< p > 3.
Lift
up
chin and tilt
head
back as far as possible.If
the
head is not tilted, the
tongue
may
block
the
throat.The
tilting
procedure
should
provide
an
open
airway
by
moving
the
tongue
away
from the back

of
the
throat.(Sometimes
the
victim
will
resume
breathing as soon as this
has
been
done.) < / p >

< p > 4.
Begin
the
resuscitation
immediately.Pinch
the
nostrils
together
with the thumb and index finger of the hand that is pressing on the victim's forehead. This prevents the loss of air through the nose during resuscitation.</p>

< p > 5.
Inhale
deeply. < / p >

< p > 6.
Place
your
mouth
tightly
around
the
victim
's mouth (over mouth and nose of small children) and blow into the air passage. Volume is important - deep breaths should be used for adults; less for children; for infants, gentle puffs (emptying the cheeks) should be sufficient. You should start at a high rate and then provide at least one breath every 5 seconds for adults and every 3 seconds for small children. Continue this maneuver so long as there is any pulse or heartbeat</p>

< p > 7.
Watch
the
victim
's chest. When you see it rise, stop blowing, raise your mouth, turn your head to the side and listen for exhalation (Fig.4).</p>

< p > 8.
If
patient is revived, keep
him
warm and do
not move
him
until
the
doctor
arrives, or at
least
for one - half hour. </ p >

< p > < b > Mouth
to
Nose
Method: < / b > < / p >

< p > What
to
do: < / p >

< p > Maintain
the
backward
head - tilt
position( as with the mouth-to-mouth method) with the hand on the forehead.Use the other hand to close the mouth.(Sometimes the victim's jaw is clenched shut as often happens in the case of drowning.

Open your mouth widely, take a deep breath, seal your mouth tightly around the victim's nose and blow into the victim's nose.

On the exhalation phase, open the victim's mouth (if possible) to allow air escape.

When administering mouth-to-nose ventilation to small children or infants, do not make the backward head-tilt as extensive as that for adults or large children.
The objective of these procedures is to obtain a rise and fall of the chest.If this is not occurring, something is
< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div2" >

< img
src = "{% static '/IMAGES/heart attack.jpg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Heart
Attack < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal2" >


Check
< / button >
< div


class ="modal fade" id="modal2" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Heart Attack < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Someone
having
a
heart
attack
may
experience
any or all
of
the
following: < / p >
< p > Uncomfortable
pressure, fullness or squeezing
pain in the
center
of
the
chest < / p >

< p > Discomfort or pain
spreading
beyond
the
chest
to
the
shoulders, neck, jaw, teeth, or one or both
arms, or occasionally
upper
abdomen < / p >

< p > Shortness
of
breath < / p >

< p > Lightheadedness, dizziness, fainting < / p >

< p > Sweating < / p >

< p > Nausea < / p >
< hr >
< p > A
heart
attack
generally
causes
chest
pain
for more than 15 minutes, but it can also have no symptoms at all.Many people who experience a heart attack have warning signs hours, days or weeks in advance.< p >

< p > < b > What
to
do if you or someone else may
be
having
a
heart
attack < / b > < / p >

< p > Call
your
local
medical
emergency
number. Don
't ignore or attempt to tough out the symptoms of a heart attack for more than five minutes. If you don'
t
have
access
to
emergency
medical
services, have
a
neighbor or a
friend
drive
you
to
the
nearest
hospital.Drive
yourself
only as a
last
resort, and realize
that
it
places
you and others
at
risk
when
you
drive
under
these
circumstances.

Chew and swallow
an
aspirin, unless
you
are
allergic
to
aspirin or have
been
told
by
your
doctor
never
to
take
aspirin.But
seek
emergency
help
first, such as calling
911.

Take
nitroglycerin, if prescribed.If you think you're having a heart attack and your doctor has previously prescribed nitroglycerin for you, take it as directed. Do not take anyone else's nitroglycerin, because that could put you in more danger.

Begin
CPR if the
person is unconscious. If
you
're with a person who might be having a heart attack and he or she is unconscious, tell the 911 dispatcher or another emergency medical specialist. You may be advised to begin cardiopulmonary resuscitation (CPR). If you haven'
t
received
CPR
training, doctors
recommend
skipping
mouth - to - mouth
rescue
breathing and performing
only
chest
compressions(about
100
per
minute).The
dispatcher
can
instruct
you in the
proper
procedures
until
help
arrives.

If
an
automated
external
defibrillator(AED) is available  and the
person is unconscious, begin
CPR
while the device is retrieved and set up.Attach the device and follow instructions that will be provided by the AED after it has evaluated the person's condition.</p>

< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div3" >

< img
src = "{% static '\IMAGES\Shock.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Shock < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal3" >


Check
< / button >
< div


class ="modal fade" id="modal3" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Shock < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< b > < p > Introduction < / p > < / b >
< hr >
< p > Shock(not to
be
confused
with emotional shock) is a life-threatening condition which happens when the body isn’t getting enough flow of blood.< / p >
< p > This
means
that
the
cells
don’t
get
enough
oxygen
to
enable
them
to
work
properly, which
can
lead
to
damage
of
the
vital
organs
like
the
brain and the
heart. < / p >

< b > < p > Shock
can
be
caused
by
anything
that
reduces
the
flow
of
blood, including: < / p > < / b >
< hr >
< p > - heart
problems, such as a
heart
attack, or heart
failure < / p >
< p > - severe
internal or external
bleeding < / p >
< p > - loss
of
body
fluids,
from dehydration, diarrhoea, vomiting or burns < / p >
< p > - severe
allergic
reactions and severe
infection < / p >

< p > If
someone
has
any
of
the
conditions
above, which
can
reduce
the
circulation or blood
flow, they
could
develop
shock, so
you
may
need
to
treat
them
for this condition as well.< / p >

< b > < p > What
to
look
for - shock< / p > < / b >
< hr >
< p > If
you
think
somebody
could
be
suffering
from shock, there

are
seven
key
things
to
look
for: < / p >

< p > 1.
Paleness
of
the
face(pallor) < / p >
< p > 2.
Cold, clammy
skin < / p >
< p > 3.
Fast, shallow
breathing < / p >
< p > 4.
Fast, weak
pulse < / p >
< p > .5.Yawning or sighing < / p >
< p > 6.
Confusion < / p >
< p > 7.
Loss
of
consciousness( in extreme
cases) < / p >

< b > < p > What
you
need
to
do - shock < / p > < / b >
< hr >

< p > If
they
are
showing
signs
of
shock: < / p >

< p > 1.
Lay
them
down
with their head low and legs raised and supported, to increase the flow of blood to their head.< / p >
< p > 2.
Call
for medical help and say you think they are in shock, and explain what you think caused it (such as bleeding or a heart attack).< / p >
< p > 3.
Loosen
any
tight
clothing
around
the
neck, chest and waist
to
make
sure
it
doesn’t
constrict
their
blood
flow < / p >
< p > 4.
Fear and pain
can
make
shock
worse, by
increasing
the
body’s
demand
for oxygen, so while you wait for help to arrive, it’s important to keep them comfortable, warm and calm.Do this by covering them with a coat or blanket and comforting and reassuring them < / p >
< p > 5.
Keep
checking
their
breathing, pulse and level
of
response. < / p >
< p > 6.
If
they
lose
consciousness
at
any
point, open
their
airway, check
their
breathing, and prepare
to
treat
someone
who
has
become
unconscious. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div4" >

< img
src = "{% static '\IMAGES\CPR.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
CPR(Cardiac
Massage) < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal4" >


Check
< / button >
< div


class ="modal fade" id="modal4" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > CPR(Cardiac Massage) < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Cardiopulmonary
resuscitation(CPR)
can
help
save
a
life
during
a
cardiac or breathing
emergency.However, even
after
training, remembering
the
CPR
steps and administering
them
correctly
can
be
a
challenge.In
order
to
help
you
help
someone in need, we
've created this simple step-by-step guide that you can print up and place on your refrigerator, in your car, in your bag or at your desk.</p>

< p > < b > Before
Giving
CPR < / b > < / p >
< hr >
< p > 1.
Check
the
scene and the
person.Make
sure
the
scene is safe, then
tap
the
person
on
the
shoulder and shout
"Are you OK?"
to
ensure
that
the
person
needs
help. < / p >
< p > 2.
Call
emergence
for assistance.If it's evident that the person needs help, call (or ask a bystander to call) emergence, then send someone to get an AED. (If an AED is unavailable, or a there is no bystander to access it, stay with the victim, call emergence and begin administering assistance.)</p>
< p > 3.
Open
the
airway.With
the
person
lying
on
his or her
back, tilt
the
head
back
slightly
to
lift
the
chin. < / p >
< p > 4.
Check
for breathing.Listen carefully, for no more than 10 seconds, for sounds of breathing.(Occasional gasping sounds do not equate to breathing.) If there is no breathing begin CPR.< / p >

< p > < b > Red
Cross
CPR
Steps < / b > < / p >
< hr >
< p > 1.
Push
hard, push
fast.Place
your
hands, one
on
top
of
the
other, in the
middle
of
the
chest.Use
your
body
weight
to
help
you
administer
compressions
that
are
at
least
2
inches
deep and delivered
at
a
rate
of
at
least
100
compressions
per
minute. < / p >
< p > 2.
Deliver
rescue
breaths.With
the
person
's head tilted back slightly and the chin lifted, pinch the nose shut and place your mouth over the person'
s
mouth
to
make
a
complete
seal.Blow
into
the
person
's mouth to make the chest rise. Deliver two rescue breaths, then continue compressions.</p>
< p > < b > Note: If
the
chest
does
not rise
with the initial rescue breath, re-tilt the head before delivering the second breath.If the chest doesn't rise with the second breath, the person may be choking. After each subsequent set of 100 chest compressions, and before attempting breaths, look for an object and, if seen, remove it.</b></p>
< p > 3.
Continue
CPR
steps.Keep
performing
cycles
of
chest
compressions and breathing
until
the
person
exhibits
signs
of
life, such as breathing, an
AED
becomes
available, or EMS or a
trained
medical
responder
arrives
on
scene. < / p >
< p > < b > Note: End
the
cycles if the
scene
becomes
unsafe or you
cannot
continue
performing
CPR
due
to
exhaustion. < / b > < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div5" >

< img
src = "{% static '\IMAGES\Swallowing tongue.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Cases
of
Swallowing
Tongue < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal5" >


Check
< / button >
< div


class ="modal fade" id="modal5" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Cases of Swallowing Tongue < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Proliferated in recent
years in sports
stadiums and the
case
of
a
dangerous
phenomenon
which is swallowing
Tongue
by
the
player and there
were
many
deaths
due
to
this
serious
situation, Mostly
be
due
to
lack
of
knowledge and how
to
aid
the
injured in this
career. < / p >

< b > < p > Tongue < / p > < / b >
< hr >
< p > Is
a
member in the
mouth is composed
of
muscle
fibers is responsible
for moving the condyle and speech < / p >

< p > < b > When
swallowing
lead
to
bridging
the
slot
soft
palate and suffocation < / b > < / p >
< hr >
< p > < b > Swallowing
the
tongue < / b > < / p >
< p > Satisfactory
condition and opposed
the
result
of
an
imbalance in the
nervous
system
have
Wania and companion
nervous
convulsions and loss
of
consciousness and memory
cache. < / p >

< p > < b > What is fact
to
swallow
the
tongue? < / b > < / p >
< hr >
< p > < b > Hear
people
say: So
people or player...Swallowing
his
tongue < / b > < / p >
< p > This
expression is wrong..Why?.Because
man is impossible
to
swallow
his
tongue < / p >
< p > So
it is wrong
to
introduce
the
hand
to
pull
the
tongue..because
the
strong
muscle
of
tongue.. and secondly
because
the
saliva
does
not help < / p >

< p > < b > What
happens if? < / b > < / p >
< p > Shahu
person
loses
consciousness, relaxes
the
whole
body, including
the
jaw and the
tongue and epiglottis.Vtsagt
Hadpallsan in the
course
of
the
air. < / p >

< p > Only
raise the
chin
to
the
top
with the tilt of the head, so as to change the slot and pulling the duct and change from round to oval < / p >

< b > < p > Causes: < / p > < / b >
< hr >
< p > - strikes
the
head and brain
concussion
head
injury
Lead
to
an
imbalance in brain
function and an
increase in electrical
stimulus
to
the
brain, convulsions, neurological and swallowing
of
the
tongue. < / p >
< p > - a
lack
of
blood
circulation, such as atrial
fibrillation
atrium
Alatjav
May
lead
to
swallowing
the
tongue and muscle
convulsions. < / p >
< p > - drop in blood
sugar
hypoglycamia
< p > - impaired
concentration
of
some
elements
such as potassium and sodium
within
the
body.

< p > < b > First
aid is the
most
important < / b > < / p >
< hr >
< p > 1.
the
medic
to
be
quiet. < / p >
< p > 2.
raising
the
head
to
the
back and the
pressure
on
the
jaw
with an attempt to push the front angle of the jaw and tongue, then will return to normal.< / p >
< p > 3.
the
medic
that is tilting
the
head
back and make
the
chin
at
the
top
level and then
followed
by
opening
the
mouth, move
the
lower
jaw
down and then
pull
out
the
tongue in a
manner
where
the
fingers
are
placed(Sbabpalibaham)
behind
him in the
form
of
a
hook and pull
out. < / p >
< p > 4. in the
event
of
difficulty
of
the
return must
insert
a
breathing
tube
endotracheal
tube
to
help
breathing
until
the
problem is solved. < / p >
< p > 5.
Use
a
stick or tool
to
flip
the
tongue
instead
of
using
fingers is the
safest
way
The
medic
may
patient
may
be
applied
to
his
mouth
on
the
medic and cut
his
fingers. < / p >

< p > < b > Notes: < / b > < / p >
< hr >
< p > - Would
be
preferable
to
put
the
patient in the
intensive
care
unit
icu < / p >
< p > - Because
he
may
need
to
Rajat
electric
booster
to
the
heart in the
case
of
a
failure in the
circulatory
system. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div6" >

< img
src = "{% static '/IMAGES/Suffocation.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Suffocation or Asphyxia < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal6" >


Check
< / button >
< div


class ="modal fade" id="modal6" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Suffocation or Asphyxia < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Asphyxia is a
condition
where
the
oxygen
level
reduces in the
blood
with an increase in the carbon dioxide concentration resulting in death or unconsciousness.< / p >

< p > < b > The
different
types
of
asphyxia
are: < / b > < / p >
< hr >
< p > -Suffocation
by
toxic
gases. < / p >
< p > -Drowning. < / p >
< p > -Choking
due
to
the
entry
of
a
foreign
substance. < / p >
< p > -Strangulation. < / p >
< p > -Asthma. < / p >
< p > -Severe
infections
of
the
throat. < / p >
< p > -Artificial
respiration. < / p >
< p > -Fetal
asphyxia. < / p >

< p > < b > First
aid
for Suffocation: < / b > < / p >
< hr >
< p > -Firstly
ensure
a
patent
airway. < / p >
< p > -Check
for the respiratory rate.< / p >
< p > -Check
for the level of cyanosis.< / p >
< p > -In
case
of
drowning, tilt
the
client
to
one
side
with head down.< / p >
< p > -If
strangulation is the
cause
then
remove
the
band
that is constricting
the
throat. < / p >
< p > -Asphyxia
caused
due
to
swelling
of
the
throat or asthma
make
the
victim
sit
upright and ensure
fresh
air. < / p >
< p > -In
case
of
suffocation
by
gases
remove
the
victim as soon as possible
to
fresh
air. < / p >
< p > -For
all
the
victims
loosen
the
clothing
surrounding
the
neck. < / p >
< p > -If
breathing
gets
restored
give
sips
of
cold
water. < / p >
< p > -If
breathing
does
not restore
then
start
artificial
respiration. < / p >

< p > The
artificial
respiration
followed is mouth - to - mouth
respiration.Follow
the
procedure
given
below: < / p >

< p > < b > Firstly
place
the
victim
on
his / her
back. < / b > < / p >

< p > -Tilt
his
head
at
the
back. < / p >
< p > -Pinch
the
nostrils. < / p >
< p > -Cover
the
mouth
of
the
casuality. < / p >
< p > -Blow
into
his
lungs
until
his
chest
expands. < / p >
< p > -Repeat
it
15 - 20
times. < / p >
< p > -Blowing
of
air
should
be
done
with an open mouth, covering both the mouth and nose.< / p >
< p > -On
the
other
hand, ensure
medical
help. < / p >
< p > -If
you
cannot
give
two
effective
breaths, start
chest
compressions. < / p >
< p > -The
first - aider
should
give
15
chest
compressions, then
give
2
inflations
to
the
lungs and then
again
start
15
chest
compressions. < / p >
< p > -The
cycle
should
be
continued
until
the
patient
recovers or till
medical
aid is called
for .< / p >

< p > < b > NOTE: < / b > < / p >
< hr >
< p > When
giving
chest
compressions
remember
to
observe
for the following: < / p >

< p > -Bluish
discoloration
of
the
face. < / p >
< p > -Dilated
pupils. < / p >
< p > -Pulse
rates(Carotid
artery).< / p >

< p > If
the
patient
recovers, let
the
victim
rest
for sometime and if he does not recover then call for the medical aid immediately.< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div7" >

< img
src = "{% static '/IMAGES/Hanging.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
First
aid
for hanging, strangling, and throttling < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal7" >


Check
< / button >
< div


class ="modal fade" id="modal7" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > First aid for hanging, strangling, and throttling < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > If
pressure is exerted
on
the
outside
of
the
neck, the
airway is squeezed and the
flow
of
air
to
the
lungs is cut
off.The
three
main
reasons or causes
why
this
could
happen
are: < / p >

< p > -hanging, suspension
of
the
body
by
a
noose
around
the
neck < / p >
< p > -strangling, constriction
around
the
neck < / p >
< p > -Throttling, squeezing
the
throat.Hanging and strangulation
may
occur
accidentally
for example, by tie or clothing caught in machinery.Ranging may also cause a broken neck, so the casualty must he handled carefully.< / p >

< p > < b > How
to
recognize? < / b > < / p >
< hr >
< p > -There
may
be
a
constricting
article
around
the
neck. < / p >
< p > -Marks
around
the
casualty’s
neck
where
a
constriction
has
been
removed. < / p >
< p > -Uneven
breathing, impaired
consciousness;
grey - blue
skin(cyanosis). < / p >
< p > -Congestion
of
the
face,
with prominent veins and possible; tiny red spots on the face or on the whites of the eyes.< / p >

< p > < b > What
to
do? < / b > < / p >
< p > -Immediately
remove
any
constriction
from around the

casualty’s
neck, Support
the
body
while you do so if it is still hanging < / p >
< p > -Do
not move
the
casualty
unnecessarily in case
of
spinal
injury < / p >
< p > -Do
not destroy or interfere
with any material, such as knotted rope, that police may need as evidence.< / p >
< p > -Lay
the
casualty
on
the
floor.Open
the
airway and check
breathing. < / p >
< p > -If
she is not breathing
be
prepared
to
resuscitate < / p >
< p > -If
she is breathing, place
her in the
recovery
position < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div8" >

< img
src = "{% static '/IMAGES/Fainting.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Fainting < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal8" >


Check
< / button >
< div


class ="modal fade" id="modal8" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Fainting < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > What
to
do: < / b > < / p >
< hr >
< p > < b > 1.
Make
the
Person
Safe < / b > < / p >

< p > -Lay
the
person
flat
on
his or her
back. < / p >
< p > -Elevate
the
person
's legs to restore blood flow to the brain.</p>
< p > -Loosen
tight
clothing. < / p >

< p > < b > 2.
Try
to
Revive
the
Person < / b > < / p >

< p > -Shake
the
person
vigorously, tap
briskly, or yell. < / p >
< p > -If
the
person
doesn
't respond, call 911 immediately and start CPR if necessary.</p>
< p > -If
an
AED is available, bring
it
by
the
person and use
it if you
have
been
trained
on
its
use. < / p >

< p > < b > Do
Home
Care
for Simple Fainting </ b > < / p >
< p > -If
the
person is alert, give
fruit
juice, especially if the
person
has
not eaten in more
than
6
hours or has
diabetes. < / p >
< p > -Stay
with the person until he or she is fully recovered.< / p >

< p > < b > Call
a
Health
Care
Provider < / b > < / p >

< p > See
a
health
care
provider
right
away if the
person: < / p >
< p > -Hit
his or her
head
when
fainting < / p >
< p > -Faints
more
than
once in a
month < / p >
< p > -Is
pregnant or has
a
heart
condition or other
serious
illness < / p >
< p > -Experiences
unusual
symptoms, such as chest
pain, shortness
of
breath, confusion, blurred
vision, or difficulty
talking < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div9" >

< img
src = "{% static '/IMAGES/Drowning.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Drownings < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal9" >


Check
< / button >
< div


class ="modal fade" id="modal9" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Drownings < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Instant
first
aid
should
be
given
to
a
person
who
has
been
rescued
from drowning, along

with immediate medical attention.< / p >

< p > < b > What
are
the
causes
of
drowning
accidents? < / b > < / p >
< hr >
< p > There
are
numerous
causes
for which people get drowned or are in near drowning situations.Some of the most common ones are:< / p >

< p > -Seizures or blows
to
the
head
when
under
water. < / p >
< p > -Attempt
to
commit
suicide. < / p >
< p > -Falling
via
thin
ice. < / p >
< p > -Consuming
alcohol
whilst
swimming, boating
etc. < / p >
< p > -Unattended
children
left
around
pools or bathtubs. < / p >
< p > -Panic
while swimming or incapability to swim.< / p >

< p > < b > Facts
related
to
drowning < / b > < / p >
< p > In
USA, thousands
drown
every
year.Most
of
the
accidents
take
place
within
close
proximities
to
safety
zones.With
immediate
first
aid and medical
attention, a
life
can
be
saved.The
concerning
victim
of
drowning, is incapable
of
even
shouting
for help.Therefore, it is important to seek for drowning signs.Children on the other hand, can drown within few inches of water only.You can revive a drowning victim, in spite of the fact that he / she has been under water for a long duration.This is possible only if the victim is young and the water – cold.Every one of us should be alert.Check whether the victim is fully clothed or not.Look out for uneven motions of swimming, which is a sign of tiredness.< / p >

< p > < b > Symptoms
of
near
drowning: < / b > < / p >
< p > 1.
Vomiting < / p >
< p > 2.
Restlessness < / p >
< p > 3.
Confusion < / p >
< p > 4.
Chest
ache < / p >
< p > 5.
Pale
appearance
of
the
victim < / p >
< p > 6.
Cold
skin < / p >
< p > 7.
Bluish
skin – mostly
around
the
victim’s
lips < / p >
< p > 8.
Abdominal
distention < / p >
< p > 9.
Unconsciousness < / p >
< p > 10.
Lack
of
breathing < / p >
< p > 11.
Lethargy < / p >
< p > 12.
Coughing
froth < / p >

< p > < b > How
to
bring
back
a
drowning
victim
on
land? < / b > < / p >
< hr >
< p > -First and foremost, as a
rescuer
you
need
to
wear
a
flotation
device
personally(only if it is available).Safety is must
for you too. </ p >
< p > -Call
911 or make
someone
call and remember
to
give
the
details
of
location
etc.thoroughly. < / p >
< p > -If
you
find
the
victim
to
be
conscious
then
try reaching him or her.The best thing to do is pull the person or grab onto him or her.< / p >
< p > -If
you’re
unable
to
reach
the
victim, use
a
rope
to
pull
him / her. < / p >
< p > -If
still
unable
to
make
the
victim
grab
onto
the
rope, tie
it
around
your
waist and then
head
out
to
the
victim.But
remember
to
tie
the
rope
to
a
boat or onto
someone and then
proceed
towards
the
victim. < / p >
< p > -You
should
keep in mind
that
you
should
not touch
a
victim
directly,
if he / she is in a panic mode.< / p >
< p > -If
the
concerning
victim is not conscious, then
you
should
take
the
boat
to
reach
him / her or
try tying the rope around your waist and pull the victim back to the shore.< / p >
< p > -After
you’ve
become
successful in bring
the
victim
out
of
the
water
safely, you
need
to
immediately
perform
first
aid.But
before
that, remember
to
remove
the
wet
clothing
from the victim’s
body and cover
him / her
with a blanket.< / p >

< p > Call
for professional assistance if only you aren’t able to rescue the victim of drowning.Every near-drowning victim should be checked by a healthcare personnel and this goes for a person who has been able to get revival.(lung issues) < / p >

< p > < b > First
aid < / b > < / p >
< hr >
< p > < b > Dos < / b > < / p >
< hr >
< p > Once
the
victim is pulled
out
of
the
water, and covered
with a blanket, check for hypothermia symptoms.If you find the victim not breathing then instantly start giving CPR.< / p >

< p > Be
cautious
when
bringing
the
victim
out
of
water.You
don’t
want
to
hurt
his / her
spine or neck( if it is already
injured).Avoid
bending or turning
his / her
neck.When
giving
CPR, make
sure
to
keep
the
neck and head
of
the
victim
still, even
when
you’re
moving
the
person. < / p >

< p > < b > The
best
thing
to
do,
for ensuring the above – is to tape the victim’s head to a stretcher or backboard.You need to secure his / her neck.To do so, place rolled up towels or similar things around the person’s neck! < / b > < / p >

< p > -First
aid
should
be
meted
out
to
victims
of
drowning
who
have
suffered
serious
injuries < / p >
< p > -Throughout
the
rescue and first
aid
process, make
sure
to
keep
the
victim
still and calm. < / p >
< p > -Keep
the
person as warm as possible, in order
to
prevent
occurrence
of
hypothermia. < / p >

< p > < b > Don’ts < / b > < / p >

< p > -Don’t
go
ahead
rescuing
the
victim
by
jumping
into
the
water,
if you’re not a trained or a swimmer yourself.< / p >
< p > -Don’t
jump
into
turbulent or rough
water. < / p >
< p > -Don’t
jump
into
ice
water.Instead
reach
out
to
the
victim
with an extended hand or object.< / p >

< p > CPR and first
aid
for drowning victim does not include the Heimlich maneuver.You should perform this protocol only if positioning the airway and rescue breathing has failed.Heimlich’s maneuver is not advised because it might make the victim vomit and choke.< / p >

< p >‘Near
drowning’ victims
need
immediate
medical
attention
because
accumulation
of
water in lungs – irrespective
of
the
amount – can
cause
constant
fluid
accumulation, which is fatal. < / p >

< p > Prevention is – any
day – better
cure.Therefore, be
cautious
when in and around
water
bodies.Avoid
alcohol
consumption, when
boating or swimming.Don’t
leave
water
standing
anywhere, even if it
a
basin, bathtub or bucket – because
drowning
can
take
place in any
water
container.Never
forget
to
keep
the
toilet
seat
cover
on(
for child safety purposes).Don’t allow children to go swimming unsupervised.Always take heed of water safety and rules.If required, take up a course in water safety, as well as, first aid and CPR! < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div10" >

< img
src = "{% static '/IMAGES/Hepatic coma.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Hepatic
Coma < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal10" >


Check
< / button >
< div


class ="modal fade" id="modal10" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Hepatic Coma < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Hepatic
coma in the
advanced
stages
of
non - cirrhotic
patients
equitable
occurs
because
of
lack
of
ability
of
the
liver
to
get
rid
of
various
toxins
nitrogen and ammonia. < / p >

< p > < b > In
the
early
stages
of
a
coma: < / b > < / p >
< hr >
< p > -The
work
of
an
enema
to
the
patient
every
6
hours. < / p >
< p > -Use
Allaktayloz
rate
of
2
tbsp
every
8
hours. < / p >
< p > -Use
Alnaoamasin
tablets
at
a
rate
of
2
tablet
every
8
hours. < / p >
< p > -Stop
taking
diuretics
medications. < / p >
< p > -Prevent
eating
foods
rich in animal
protein < / p >

< p > < b > In
case
of
severe
coma: < / b > < / p >
< hr >
< p > The
patient
should
be
transferred
to
the
hospital
where
the
patient in this
case
needs
for medical care and private nursing, and also to determine the cause of the coma as some cases coma may be accompanied by internal bleeding from esophageal varices.< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div11" >

< img
src = "{% static '/IMAGES/Diabetic emergency.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Diabetic
emergency < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal11" >


Check
< / button >
< div


class ="modal fade" id="modal11" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Diabetic emergency < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Diabetes is a
lifelong
medical
condition
where
the
body
cannot
produce
enough
insulin.Insulin is a
chemical
made
by
the
pancreas(a
gland
behind
the
stomach), which
regulates
the
blood
sugar(glucose)
level in the
body. < / p >

< p > Normally
our
bodies
automatically
keep
the
right
blood
sugar
levels, but
for someone with diabetes their body can't. Instead, they have to control the blood suger level themselves by monitoring what they eat, and taking insulin injections or pills.</p>

< p > There
are
two
types
of
diabetes: Type1, or insulin - dependent
diabetes, and Type
2, also
known as non - insulin - dependent
diabetes. < / p >

< p > Sometimes
people
who
have
diabetes
may
have
a
diabetic
emergency, where
their
blood
sugar
becomes
either
too
high or too
low.Both
conditions
are
potentially
serious and may
need
treatment in hospital. < / p >

< p > < b > Hyperglycaemia < / b > < / p >
< hr >
< p > Too
little
insulin
can
cause
high
blood
sugar(hyperglycaemia). < / p >

< p > If
it’s
not treated and gets
worse, the
person
can
gradually
become
unresponsive(going
into
a
diabetic
coma).So
it
's important to get them to see a doctor in case they need emergency treatment.</p>

< p > < b > Hypoglycaemia < / b > < / p >
< hr >
< p > Too
much
insulin
can
cause
low
blood
sugar or hypoglycaemia(hypo). < / p >

< p > This
often
happens
when
someone
with diabetes misses a meal or does too much exercise.It can also happen after someone has had an epileptic seizure or has been binge drinking.< / p >

< p > If
someone
knows
they
are
diabetic, they
may
recognise
the
start
of
a
hypo
attack, but
without
help
they
may
quickly
become
weak and unresponsive. < / p >

< p > < b > What
to
look
for - Diabetic emergency </ b > < / p >
< hr >
< p > If
you
think
someone is having
a
diabetic
emergency, you
need
to
check
against
the
symptoms
listed
below
to
decide if their
blood
sugar is too
high or too
low. < / p >

< p > < b > High
blood
sugar(hyperglycaemia) < / b > < / p >
< p > -Warm, dry
skin < / p >
< p > -Rapid
pulse and breathing < / p >
< p > -Fruity
sweet
breath < / p >
< p > -Really
thirsty < / p >
< p > -Drowsiness, leading
to
unresponsiveness if not treated < / p >

< p > < b > Low
blood
sugar(hypoglycaemia) < / b > < / p >
< p > -Weakness, faintness or hunger < / p >
< p > -Confusion and irrational
behaviour < / p >
< p > -Sweating
with cold, clammy skin < / p >
< p > -Rapid
pulse < / p >
< p > -Trembling < / p >
< p > -Deteriorating
level
of
response < / p >
< p > -Medical
warning
bracelet or necklace and glucose
gel or sweets < / p >
< p > -Medication
such as an
insulin
pen or tablets and a
glucose
testing
kit < / p >

< p > < b > What
you
need
to
do ‒ for high blood sugar (hyperglycaemia) < / b > < / p >
< hr >
< p > -Call
for medical help and say that you suspect hyperglycaemia.< / p >
< p > -While
you
wait
for help to arrive, keep checking their breathing, pulse and level of response.< / p >
< p > -If
they
lose
responsiveness
at
any
point, open
their
airway, check
their
breathing and prepare
to
treat
someone
who’s
become
unresponsive. < / p >

< p > < b > What
you
need
to
do ‒ for low blood sugar (hypoglycaemia) < / b > < / p >
< p > Help
them
sit
down.If
they
have
their
own
glucose
gel, help
them
take
it.If
not, you
need
to
give
them
something
sugary
like
fruit
juice, a
fizzy
drink, two
teaspoons
of
sugar, or sugary
sweets. < / p >

< p > If
they
improve
quickly, give
them
more
sugary
food or drink and let
them
rest.If
they
have
their
glucose
testing
kit
with them, help them use it to check their glucose level.Stay with them until they feel completely better.< / p >

< p > If
they
do
not improve
quickly, look
for any other causes and then call 999 or 112 for medical help.< / p >

< p > While
waiting, keep
checking
their
responsiveness, breathing and pulse. < / p >

< p > < b > What
you
need
to
do ‒ if you’re unsure whether their blood sugar is high or low < / b > < / p >
< hr >
< p > If
you’re
not sure
whether
someone
has
high or low
blood
sugar, give
them
something
sugary
anyway, as this
will
quickly
relieve
low
blood
sugar and is unlikely
to
do
harm in cases
of
high
blood
sugar < / p >

< p > If
they
don’t
improve
quickly, call
999 or 112
for medical help. </ p >

< p > If
they
lose
responsiveness
at
any
point, open
their
airway, check
their
breathing and prepare
to
treat
someone
who’s
become
unresponsive. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div12" >

< img
src = "{% static '/IMAGES/Case of death.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Diagnosed
case
of
death < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal12" >


Check
< / button >
< div


class ="modal fade" id="modal12" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Diagnosed case of death < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Confirmed
signs
of
the
death
of
a
person < / b > < / p >
< hr >
< p > You
can
even
diagnose
the
case
of
death, feel
your
pulse and breathing
person,
if it is completely shut in a quarter of an hour at least, and artificial respiration and CPR attempts did not work with him, the presence of a sign or more of the following marks mentioned are the testimony stressing the case of death:< / p >

< p > -When
directing
the
light(the
Scouts,
for example) to the appointed person for about 10 seconds continuously not find any reaction to the human eye (the eye Nunn Eye Pupil), and if it is still alive will narrow the human eye when the light guide and can accommodate at blocking light.< / p >
< p > -Try
entering
your
middle
finger in the
person
's mouth until it reaches the throat, if alive, would lead to vomit, but in the absence of reaction to this is a sign of death.</p>
< p > -Sensing
the
degree
of
public and private
limbs
of
his
body
heat,
if it was cool supportive evidence of his death.< / p >
< p > -The
presence
of
white
liquid
foam
coming
out
of
his
mouth is further
evidence
supportive
of
his
death. < / p >
< p > -Sag
lower
jaw
of
the
mouth. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div13" >

< img
src = "{% static '/IMAGES/Stroke.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Stroke < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal13" >


Check
< / button >
< div


class ="modal fade" id="modal13" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Stroke < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > A
stroke
happens
when
the
flow
of
blood
to
part
of
the
brain is cut
off.This is normally
due
to
a
clot in a
blood
vessel or a
rupture
which
stops
the
flow
of
blood
getting
to
the
brain.The
brain
needs
the
oxygen in the
blood
to
work
properly.Lack
of
oxygen
causes
damage
to
the
brain
cells.The
long - term
effects
of
a
stroke
depend
on
which
part
of
the
brain is affected and how
large
an
area is damaged.A
stroke( or brain
attack) is a
medical
emergency - you
need
to
act
fast. < / p >

< p > < b > What
to
look
for - Stroke< / b > < / p >
< hr >
< p > If
you
think
someone is having
a
stroke, check
the
three
main
symptoms
using
the
FAST
test: < / p >

< p > < b > Face < / b > ‒ look
at
their
face and ask
them
to
smile.Are
they
only
able
to
smile
on
one
side
of
their
mouth? If
yes, this is not normal. < / p >
< p > < b > Arms < / b > ‒ ask
them
to
raise both
arms.Are
they
only
able
to
lift
one
arm? If
yes, this is not normal. < / p >
< p > < b > Speech < / b > ‒ ask
them
to
speak.Are
they
struggling
to
speak
clearly? If
yes, this is not normal. < / p >
< p > < b > Time < / b > ‒ if the answer to any of these three questions is yes, then it is time to call 999 or 112 for medical help and say you think the casualty is having a stroke.< / p >

< p > < b > What
you
need
to
do - Stroke < / b > < / p >
< hr >
< p > -While
you
wait
for help to arrive, keep them comfortable and supported.If they’re responsive then you can help them into a comfortable position < / p >
< p > -Keep
checking
their
breathing, pulse and level
of
response.Don’t
give
them
anything
to
eat or drink
because
it
could
be
difficult
for them to swallow so they might choke.< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div14" >

< img
src = "{% static '/IMAGES/Burns and scalds.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Burns and Scalds < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal14" >


Check
< / button >
< div


class ="modal fade" id="modal14" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Burns and Scalds < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Burns and scalds
are
damage
to
the
skin
caused
by
heat.A
burn is usually
caused
by
dry
heat, like
fire, a
hot
iron, or the
sun.A
scald is caused
by
wet
heat, like
steam or a
hot
cup
of
tea. < / p >

< p > You
need
to
be
extra
careful
when
treating
burns.The
longer
the
burning
goes
on, the
more
severe
the
injury
will
be, and the
longer
it
may
take
to
heal.So
you
need
to
cool
the
burn as soon as possible. < / p >

< p > If
someone
has
a
severe
burn or scald
they
are
likely
to
suffer
from shock, because

of
the
fluid
loss, so
they
will
need
urgent
hospital
treatment. < / p >

< p > < b > What
to
look
for < / b > < / p >
< hr >
< p > If
you
think
someone
has
a
burn or scald, there
are
five
key
things
to
look
for: < / p >

< p > -Red
skin < / p >
< p > -Swelling < / p >
< p > -Blisters
may
form
on
the
skin
later
on < / p >
< p > -The
skin
may
peel < / p >
< p > -The
skin
may
be
white or scorched < / p >

< p > < b > What
you
need
to
do < / b > < / p >
< hr >
< p > Stop
the
burning
getting
any
worse, by
moving
the
casualty
away
from the source

of
heat. < / p >

< p > Start
cooling
the
burn as quickly as possible.Run
it
under
cool
water
for at least ten minutes or until the pain feels better.(Don’t use ice, creams or gels – they can damage tissues and increase risk of infection).< / p >

< p > Assess
how
bad
the
burn is.It is serious
if it is: < / p >

< p > -larger
than
the
size
of
the
casualty
's hand</p>
< p > -on
the
face, hands or feet < / p >
< p > -a
deep
burn < / p >

< p > If
it is serious, call
for emergency medical help.< / p >

< p > Remove
any
jewellery or clothing
near
the
burn(unless
it is stuck
to
it).< / p >

< p > Cover
the
burned
area
with kitchen cling film or another clean, non-fluffy material, like a clean plastic bag.This will protect from infection.< / p >
< p > If
necessary, treat
for shock(shock is a life - threatening condition, not to be confused with emotional shock).< / p >

< p > If
you
are
unsure if the
burn is serious
then
tell
the
person
to
see
a
doctor. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div15" >

< img
src = "{% static '/IMAGES/heatstroke.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Heatstroke < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal15" >


Check
< / button >
< div


class ="modal fade" id="modal15" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Heatstroke < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Heatstroke is caused
by
a
failure
of
the
thermostat in the
brain
which
regulates
the
body
temperature.If
someone
has
a
high
fever or has
been
exposed
to
heat
for a long time, then their body can become dangerously overheated.< / p >

< p > Someone
can
also
get
heatstroke
after
using
drugs
such as ecstasy. < / p >

< p > Sometimes, people
get
heatstroke
after
suffering
from heat exhaustion.When
someone
gets
too
dehydrated
they
stop
sweating
which
means
their
body
can’t
cool
down
anymore, so
they
develop
heatstroke. < / p >

< p > Heatstroke
can
develop
with very little warning, causing unresponsiveness within minutes of someone feeling unwell.Your priority is to cool them down as quickly as possible and get them to hospital.< / p >

< p > < b > What
to
look
for - heatstroke< / b > < / p >
< hr >
< p > These
are
the
six
key
things
to
look
for: < / p >

< p > -Headache, dizziness and discomfort < / p >
< p > -Restlessness and confusion < / p >
< p > -Hot
flushed and dry
skin < / p >
< p > -A
fast
deterioration in the
level
of
response < / p >
< p > -A
full
bounding
pulse < / p >
< p > -Body
temperature
above
40°C(104°F) < / p >

< p > < b > What
you
need
to
do - heatstroke < / b > < / p >
< hr >
< p > -Quickly
move
them
to
a
cool
place and remove
their
outer
clothing
but
ensure
you
maintain
their
dignity. < / p >
< p > -Then
call
999 / 112
for an ambulance. </ p >
< p > -Wrap
them in a
cold
wet
sheet and keep
pouring
cold
water
over
it
until
their
temperature
falls
to
at
least
38°C( or 100.4°F).Measure
this
with a thermometer under their tongue or under their armpit.< / p >
< p > -If
you
can’t
find
a
sheet, fan
them or sponge
them
down
with cold water to keep them cool.< / p >
< p > -Once
their
temperature
seems
to
have
gone
back
to
normal, replace
the
wet
sheet
with a dry sheet.< / p >
< p > -While
waiting
for help to arrive, keep checking their temperature, as well as their breathing, pulse and level of response.< / p >
< p > -If
they
start
getting
hot
again, repeat
the
cooling
process
to
lower
their
temperature. < / p >
< p > -If
they
lose
responsiveness
at
any
point, open
their
airway, check
their
breathing and prepare
to
treat
someone
who’s
become
unresponsive. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div16" >

< img
src = "{% static '/IMAGES/Heat exhaustion.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Heat
Exhaustion < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal16" >


Check
< / button >
< div


class ="modal fade" id="modal16" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Heat Exhaustion < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Heat
exhaustion is caused
by
a
loss
of
salt and water
from the body, usually

through
excessive
sweating. < / p >

< p > It
develops
slowly and usually
happens
to
people
who
aren’t
used
to
hot, humid
weather.People
who
are
unwell
are
more
likely
to
get
it, especially if they
are
suffering
from vomiting and diarrhoea. < / p >

< p > A
dangerous and common
cause
of
heat
exhaustion is when
the
body
produces
more
heat
than
it
can
cope
with.< / p >

< p > This
can
happen
when
someone
takes
a
non - prescription
drug, like
ecstasy, which
can
stop
the
body
from regulating its

temperature
properly.If
someone
gets
hot and sweats
a
lot
from dancing as well, they

may
get
overheated and dehydrated, giving
them
heat
exhaustion. < / p >

< p > If
treated
quickly, someone
suffering
from heat exhaustion

should
start
feeling
better
quickly.But if not treated, they
could
develop
heatstroke
which
can
lead
to
death. < / p >

< p > < b > What
to
look
for - Heat exhaustion </ b > < / p >
< hr >
< p > These
are
the
six
key
things
to
look
for: < / p >

< p > -Headache < / p >
< p > -Dizziness and confusion < / p >
< p > -Loss
of
appetite and feeling
sick < / p >
< p > -Sweating
with pale clammy skin < / p >
< p > -Cramps in the
arms, legs and stomach < / p >
< p > -Fast, weakening
pulse and shallow
breathing < / p >

< p > < b > What
you
need
to
do - Heat
exhaustion < / b > < / p >
< hr >
< p > -Help
take
them
to
a
cool
place and get
them
to
lie
down
with their legs raised.< / p >
< p > -Then
give
them
lots
of
water.You
can
also
give
them
a
sports
drink
like
Lucozade or an
oral
rehydration
solution
to
help
replace
the
salt and fluid
they
have
lost
by
sweating. < / p >
< p > -Keep
checking
their
breathing, pulse and level
of
response. < / p >
< p > -Even if they
recover
quickly, suggest
they
see
a
doctor. < / p >
< p > -If
they
seem
to
be
getting
worse, place
them
into
the
recovery
position and call
for an ambulance. </ p >
< p > -While
waiting, keep
checking
their
breathing, pulse and level
of
response. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div17" >

< img
src = "/IMAGES/frostbite.jpeg"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Frostbite < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal17" >


Check
< / button >
< div


class ="modal fade" id="modal17" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Frostbite < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Frostbite
happens
when
parts
of
the
skin and other
tissues
freeze
due
to
low
temperatures.Frostbite
usually
affects
the
fingers and toes as they
are
the
parts
of
the
body
furthest
from the heart.< / p >

< p > If
someone
has
severe
frostbite
then
they
might
permanently
lose
all
feeling in that
part
of
their
body.Frostbite
can
also
lead
to
gangrene, when
the
blood
vessels and soft
tissues
become
permanently
damaged
leading
to
death
of
the
tissue. < / p >

< p > Frostbite
usually
happens in freezing or cold and windy
weather.People
who
cannot
move
around
are
more
likely
to
get
it.Someone
with frostbite will probably have hypothermia, so be prepared to treat them for that too.< / p >

< p > < b > What
to
look
for - frostbite< / b > < / p >
< hr >
< p > If
you
think
someone
has
frostbite, there
are
four
key
things
to
look
for: < / p >

< p > -‘Pins and needles’ to
begin
with< / p >
< p > -Paleness, followed
by
numbness < / p >
< p > -Hardening and stiffening
of
the
skin < / p >
< p > -Change in skin
colour: first
white, then
blotchy and blue.On
recovery, the
skin
may
be
red, hot, painful and blistered.If
they
get
gangrene, the
tissue
may
become
black
due
to
the
loss
of
blood
supply and death
of
the
tissue. < / p >

< p > < b > What
you
need
to
do - frostbite < / b > < / p >
< hr >
< p > -First, encourage
them
to
put
their
hands in their
armpits.Then
help
move
them
indoors or to
somewhere
warm. < / p >
< p > -Once
inside, gently
remove
anything
constricting
like
rings, gloves or boots. < / p >
< p > -Next, warm
the
body
part
with your hands on your lap, or under their armpits.Don’t rub it though because this could damage their skin tissue.(If there is a danger of it refreezing then don’t warm it up yet as this can cause more damage).< / p >
< p > -Place
the
body
part in warm(not hot)
water
at
around
40°C(104°F) and be
careful
not to
put
it
near
direct
heat as this
can
cause
more
damage.Dry
it
carefully and put
on
a
light
dressing, ideally
a
gauze
bandage
from your first

aid
kit. < / p >
< p > -Once
you’ve
done
that, help
them
to
raise their
limb
to
reduce
swelling,
with cushions or a sling for instance.< / p >
< p > -Advise
them
to
take
some
painkillers if they
have
some(paracetamol for example). < / p >
< p > -Then
take or send
them
to
hospital, keeping
their
limb
raised. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div18" >

< img
src = "{% static '/IMAGES/fever.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Fever < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal18" >


Check
< / button >
< div


class ="modal fade" id="modal18" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Fever < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > A
fever is a
high
temperature.When
someone’s
body
temperature
goes
above
the
normal
body
temperature
of
37°C(98.
6°F), this is called
a
fever. < / p >

< p > Usually
fevers
are
caused
by
infections or illnesses, such as a
sore
throat, earache, or chickenpox. < / p >

< p > Fevers
are
common in children and, though
worrying
for parents, they often go away without treatment.< / p >

< p > But if a
young
child’s
temperature
goes
above
39°C(102.
2°F) this
can
be
dangerous and might
trigger
a
seizure(fit). < / p >

< p > < b > What
to
look
for - Fever< / b > < / p >
< hr >
< p > These
are
the
six
key
things
to
look
for when someone has a fever:< / p >

< p > < b > Early
signs
of
fever: < / b > < / p >

< p > -High
temperature - above
37°C(98.
6°F) < / p >
< p > -Pale
skin < / p >
< p > -They
may
feel
cold,
with goose pimples, shivering and chattering teeth < / p >

< p > < b > Then, later: < / p > < / p >

< p > -Hot, flushed
skin and sweating < / b >
< p > -Headache < / p >
< p > -General
aches and pains < / p >

< p > < b > What
you
need
to
do - Fever < / b > < / p >
< hr >
< p > -If
you
notice
some
of
these
symptoms, take
their
temperature
using
a
thermometer. < / p >
< p > -If
their
temperature is above
37°C, it’s
a
fever. < / p >
< p > -Help
make
them
comfortable and keep
them
cool, ideally in bed
with a sheet or light duvet.< / p >
< p > -Give
them
plenty
of
cool
drinks
to
replace
any
fluid
they
lose
from sweating. < / p >
< p > -If
they’re
feeling
unwell, you
can
give
them
the
recommended
dose
of
paracetamol(remember - don’t
give
aspirin - based
medication
to
anyone
under
16).< / p >
< p > -Check
their
breathing, pulse and level
of
response
until
they’re
feeling
better. < / p >
< p > -If
you’re
worried
about
their
condition
then
call
their
local
doctor’s
surgery, or NHS
advice
line
for free on 111 for advice in England and Scotland ( for Wales call 0845 46 47).< / p >
< p > -If
their
temperature is above
39°C, call
the
doctor, or the
NHS
advice
line
for free on 111 for advice in England and Scotland ( for Wales call 0845 46 47).< / p >
< p > -If
they
seem
to
be
getting
worse
then
call
999 / 112
for emergency medical help and be prepared to treat them for a seizure.< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div19" >

< img
src = "{% static '/IMAGES/food poisoning.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Food
Poisoning < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal19" >


Check
< / button >
< div


class ="modal fade" id="modal19" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Food Poisoning < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Food
poisoning is caused
by
eating
contaminated
food.In
most
cases
the
food
hasn’t
been
cooked
properly and is contaminated
by
bacteria
such as salmonella or Escherichia
coli(E.coli), which
are
found
mainly in meat. < / p >

< p > Someone
may
feel
the
effects
of
food
poisoning
within
a
few
hours, and will
often
be
sick or have
diarrhoea.However, in some
cases
it
can
take
up
to
three
days. < / p >

< p > The
effects
of
food
poisoning
can
make
someone
feel
extremely
ill.The
most
important
thing is
for you to keep encouraging the person to drink water so they don’t get dehydrated.Most people will get better without needing treatment.< / p >

< p > < b > What
to
look
for - Food poisoning </ b > < / p >
< hr >
< p > If
you
think
someone
may
have
food
poisoning, these
are
the
five
key
things
to
look
for: < / p >

< p > -Feeling
sick < / p >
< p > -Vomiting, sometimes
bloodstained < / p >
< p > -Stomach
cramps < / p >
< p > -Diarrhoea < / p >
< p > -Headache or fever < / p >

< p > < b > What
you
need
to
do - Food
poisoning < / b > < / p >
< hr >
< p > -If
you
notice
any
of
these
symptoms, tell
the
person
to
lie
down and rest. < / p >
< p > -Give
them
plenty
of
water and a
bowl
to
use in case
they
are
sick. < / p >
< p > -Encourage
them
to
drink as much
water as they
can, even if they
can
only
manage
regular
small
sips.If
they
have
diarrhoea, it’s
even
more
important
that
they
drink
water
to
replace
lost
fluids. < / p >
< p > -Giving
them
an
oral
rehydration
solution is good
to
way
to
replace
fluids
lost
through
diarrhoea and vomiting.This
solution
can
replace
salt and other
minerals
which
they
have
lost.You
can
buy
it in a
pharmacy as a
sachet
which
you
dissolve in water. < / p >
< p > -If
the
person
gets
worse, then
advise
them
to
call
their
doctor or call
for emergency medical help.< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div20" >

< img
src = "{% static '/IMAGES/bumps and bruises.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Bumps and bruises < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal20" >


Check
< / button >
< div


class ="modal fade" id="modal20" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Bumps and bruises < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > After
someone
has
had
an
injury
to
the
skin, they’ll
often
get
a
bump or a
bruise.Bumps and bruises
may
not appear
straight
away
but
the
skin
can
still
be
painful and often
feel
tender or swollen
at
first. < / p >

< p > Bumps
are
swellings
caused
by
fluid
under
the
surface
of
the
skin. < / p >

< p > Bruises
are
bluish or purple - coloured
patches
that
appear
because
tiny
blood
vessels
beneath
the
skin
burst and leak
blood
into
the
soft
tissue.As
they
heal, bruises
usually
change
to
a
yellowish
green
colour. < / p >

< p > < b > What
you
need
to
do < / b > < / p >
< hr >
< p > If
someone
has
a
bump or bruise, hold
something
cold
onto
the
skin
straight
after
the
injury
to
help
it
heal and reduce
the
pain.This
could
be
a
bag
of
peas or ice
wrapped in a
cloth, or a
cold
compress if you
have
one.Do
not leave
it
on
for more than ten minutes.< / p >

< p > If
the
injury is painful
then
help
them
to
lie
down and
raise the
area
above
their
heart,
if possible, to help slow the flow of blood to the area and so reduce the swelling.< / p >

< p > If
a
bump or bruise
becomes
very
swollen or very
painful, then
you
should
tell
them
to
see
a
healthcare
professional
for advice.< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div21" >

< img
src = "{% static '/IMAGES/severe bleeding.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Severe
Bleeding < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal21" >


Check
< / button >
< div


class ="modal fade" id="modal21" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Severe Bleeding < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > When
bleeding is severe, it
can
be
dramatic and distressing.If
someone’s
bleeding
isn’t
controlled
quickly, they
may
develop
shock and lose
consciousness.Shock
does
not mean
emotional
shock, but is a
life - threatening
condition, often
caused
by
loss
of
blood. < / p >

< p > If
someone’s
bleeding
from their mouth or nose, they
may
find
it
hard
to
breathe, so
you
should
keep
a
close
eye
on
them in case
they
become
unresponsive. < / p >

< p > If
there’s
an
object in their
wound, don
't press directly onto it, as it will hurt, but leave it in there and bandage around it.</p>

< p > With
all
open
wounds, there’s
a
risk
of
infection, so
wash
your
hands and use
gloves( if you
have
any) to
help
prevent
any
infection
passing
between
you
both. < / p >

< p > < b > What
you
need
to
do - severe
bleeding < / b > < / p >
< hr >
< p > Your
priority is to
stop
the
bleeding.Protect
yourself
by
wearing
gloves. < / p >

< p > If
the
wound is covered
by
the
casualty
's clothing, remove or cut the clothes to uncover the wound.</p>

< p > < b > If
there
an
object in the
wound < / b > < / p >

< p > If
there’s
an
object in there, don’t
pull
it
out, because
it
may
be
acting as a
plug
to
reduce
the
bleeding.Instead, leave
it in and apply
pressure
either
side
of
it
with a pad (such as a clean cloth) or fingers, until a sterile dressing is available.< / p >

< p > < b > If
there
's no object in the wound</b></p>

< p > Follow
the
steps
below
for treating severe bleeding.< / p >

< p > < b > Step
1
of
2: Press
it < / b > < / p >
< p > Put
direct
pressure
on
the
wound
with your fingers, using a sterile dressing if possible, to stop blood escaping.< / p >

< p > < b > Step
2
of
2: Call
for medical help </ b > < / p >
< p > Waiting
for help< / p >
< p > -Firmly
wrap
a
bandage
around
the
pad or dressing
on
top
of
the
wound
to
control
the
bleeding.Make
it
firm
enough
to
maintain
pressure
but
not so
tight
that
it
restricts
their
circulation. < / p >
< p > -Treat
them
for shock: lay
them
down
with their head low and thier legs raised and supported.< / p >
< p > -If
blood
shows
through
the
pad or dressing, don’t
remove
it: apply
a
second
dressing
on
top
of
the
first
one.If
blood
then
seeps
through
both
dressings, remove
both
of
them and replace
them
with a fresh dressing.When changing dressings, make sure you keep pressure applied to where the bleeding is coming from .< / p >
< p > -If
you
can, support
the
injured
area.For
example, you
can
rest
a
leg
on
some
cushions, or for an arm you can make a sling.< / p >
< p > -Keep
checking
the
casualty
's breathing, pulse and level of response.</p>
< p > -If
they
become
unresponsive
at
any
point, open
their
airway, check
their
breathing, and prepare
to
treat
someone
who
has
become
unresponsive. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div22" >

< img
src = "{% static '/IMAGES/nose bleeds.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Nose
bleeds < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal22" >


Check
< / button >
< div


class ="modal fade" id="modal22" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Nose bleeds < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > A
nose
bleed is when
blood
flows
from one or both
nostrils.It’s
normally
caused
by
the
tiny
blood
vessels
inside
the
nostrils
being
ruptured. < / p >
< p > Common
causes
of
nose
bleeds
include
a
blow
to
the
nose, sneezing, picking or blowing
the
nose, and high
blood
pressure. < / p >

< p > < b > What
to
look
for - Nose bleeds </ b > < / p >
< hr >
< p > Most
nose
bleeds
are
minor and only
last
a
few
minutes, but
they
can
be
dangerous if someone
loses
a
lot
of
blood. < / p >

< p > If
someone
has
had
a
blow
to
the
head, the
blood
may
appear
thin and watery.This
could
mean
that
their
skull is fractured and fluid is leaking
from around the

brain.If
that
happens, it is very
serious and you
should
call
for emergency medical help.See advice for head injuries.< / p >

< p > < b > What
to
do - Nose
bleeds < / b > < / p >
< hr >
< p > If
someone is having
a
nose
bleed, your
priority is to
control
the
bleeding and keep
their
airway
open. < / p >

< p > Get
them
to
sit
down(not lie
down) as keeping
the
nose
above
the
heart
will
reduce
bleeding. < / p >

< p > Get
them
to
lean
forward(not backwards), to
make
sure
the
blood
drains
out
through
their
nose, rather
than
down
their
throat
which
could
block
their
airway. < / p >

< p > Ask
them
to
breathe
through
their
mouth and pinch
the
soft
part
of
the
nose, taking
a
brief
pause
every
ten
minutes, until
the
bleeding
stops. < / p >

< p > Encourage
them
not to
speak, swallow, cough, spit or sniff
because
this
may
break
blood
clots
that
may
have
started
to
form in the
nose. < / p >

< p > If
the
bleeding is severe, or if it lasts more than 30 minutes, call 999 or 112 for medical help.< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div23" >

< img
src = "{% static '/IMAGES/Ear treatment.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Ear
Foreign
Body
Treatment < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal23" >


Check
< / button >
< div


class ="modal fade" id="modal23" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Ear Foreign Body Treatment < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > 1.
Remove
Object if Possible < / b > < / p >
< hr >
< p > -If
you
can
see
the
foreign
body in the
ear and remove
it
easily, carefully
do
so
using
tweezers.Never
poke
at
the
ear or
try to remove the object by force.< / p >
< p > -Tilt
the
head
to
try to help the object fall out.< / p >
< p > -If
it is a
live
insect, you
can
kill
it
for easier removal by putting a few drops of baby oil or vegetable oil in the ear.Have the person tilt and gently shake his or her head to dislodge the object.Don't use this method for anything other than an insect, and don't use it if there is any pain or bleeding or if the person has tubes in the ear.< / p >
< p > -If
you
can
't see the object or can'
t
remove
it
easily, or if removing it will cause pain, call your health care provider.< / p >

< p > < b > 2.
Do
Not
Try
to
Remove
Earwax < / b > < / p >
< hr >
< p > -If
you
believe
earwax is causing
ear
discomfort or hearing
loss, see
a
health
care
provider.Don
't use cotton swabs. They can push earwax deeper into the ear. Other earwax removal methods can cause ear damage.</p>

< p > < b > 3.
When
to
See
a
Health
Care
Provider < / b > < / p >
< hr >
< p > See
a
health
care
provider
immediately if: < / p >

< p > -You
cannot
remove
the
foreign
body
easily
by
yourself or if parts
of
the
object
remain in the
ear. < / p >
< p > -Pain is severe. < / p >
< p > -Pain, hearing
loss, or discomfort
continues
after
the
object is removed. < / p >

< p > < b > 4.
Follow
Up < / b > < / p >
< hr >
< p > If
the
person
sees
a
health
care
provider, the
next
steps
depend
on
the
particular
case. < / p >

< p > -The
health
care
provider
will
remove
the
object
by
using
tweezers, by
flushing
it
with water, or by using another removal method.< / p >
< p > -The
health
care
provider
may
give
the
person
antibiotic
eardrops if the
ear
has
been
injured or shows
signs
of
infection. < / p >
< p > -If
earwax is affecting
hearing or causing
discomfort, the
health
care
provider
may
use
a
special
tool
to
remove
it. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div24" >

< img
src = "{% static '/IMAGES/broken tooth.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Broken or Knocked - Out
Teeth < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal24" >


Check
< / button >
< div


class ="modal fade" id="modal24" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Broken or Knocked-Out Teeth < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > A
knocked - out
permanent
tooth is a
dental
emergency.Knocked - out
teeth
can
be
re - implanted in many
cases.A
permanent
tooth
that is re - implanted
within
30
minutes
has
the
highest
chance
of
success. < / p >

< p > < b > 1.
Collect
Teeth or Teeth
Fragments < / b > < / p >
< hr >
< p > -Handle
teeth
carefully
because
damage
may
prevent
re - implantation. < / p >
< p > -Touch
only
the
crown, the
top
part
of
the
tooth.Do
not touch
the
root
of
the
tooth. < / p >
< p > -Rinse
the
tooth
gently in a
bowl
of
lukewarm
water
for no more than 10 seconds only if there is dirt or foreign matter on it.Do not scrub, scrape, or use alcohol to remove dirt.< / p >

< p > < b > 2.
Re - Insert or Store
Teeth < / b > < / p >
< hr >
< p > -Rinse
mouth
with warm water.< / p >
< p > -If
possible, reinsert
permanent
teeth
into
the
correct
sockets and have
the
person
bite
on
a
gauze
pad
to
hold
teeth in place. < / p >
< p > -If
you
can
't reinsert permanent teeth, or for baby teeth or teeth fragments, store them in whole milk or between your cheek and gum to prevent drying.</p>

< p > < b > 3.
Treat
Symptoms < / b > < / p >
< hr >
< p > -Control
bleeding
with sterile gauze or cloth.< / p >
< p > -For
pain and swelling, apply
a
cool
compress.Encourage
a
child
to
suck
on
a
frozen
pop. < / p >
< p > -For
pain, take
ibuprofen or acetaminophen. < / p >

< p > < b > 4.
Get
Help < / b > < / p >
< hr >
< p > -For
teeth
that
have
been
knocked
out, see
a
dentist or go
to
an
emergency
room
immediately.Take
the
teeth or teeth
fragments
with you.Even if the teeth have been successfully reinserted, you should see a dentist.< / p >
< p > -For
chipped or broken
teeth, call
a
dentist. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div25" >

< img
src = "{% static '/IMAGES/eye injury.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Eye
injuries < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal25" >


Check
< / button >
< div


class ="modal fade" id="modal25" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Eye injuries < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Eye
injuries
vary
from something very

minor, such as getting
shampoo in your
eye, to
something
quite
serious, such as a
cut, which
could
cause
permanent
loss
of
vision. < / p >

< p > Common
types
of
eye
injury
include: < / p >

< p > -foreign
objects
getting
stuck in the
eye, like
an
eyelash or pieces
of
grit, wood or metal < / p >
< p > -cuts or grazes,
from sharp objects

like
glass or metal < / p >
< p > -severe
blows
to
the
eye,
from a hard

object, like
a
ball. < / p >

< p > Foreign
objects
like
grit, or a
loose
eyelash, often
land
on
the
surface
of
the
eye.Usually
you
can
easily
rinse
these
out
but
sharp
fragments
like
grit, metal or glass
may
cut
the
eye in which
case
the
person
should
go
to
hospital. < / p >

< p > All
eye
injuries
are
potentially
serious
because
they
could
damage
the
person’s
vision.Even
grazes
to
the
surface
of
the
eye, called
the
cornea, can
lead
to
scarring or infection, which
could
permanently
damage
someone
's vision.</p>

< p > < b > What
to
look
for - eye injuries </ b > < / p >
< hr >
< p > < b > The
five
key
things
to
look
for are: < / b > < / p >
< p > 1.
Pain in the
eye or eyelid < / p >
< p > 2.
A
visible
wound or bloodshot
appearance < / p >
< p > 3.
Partial or total
loss
of
vision < / p >
< p > 4.
Blood or a
clear
fluid
leaking
from a wound < / p >
< p > 5.
Screwed
up
eyelids and watering if there’s
something in there < / p >

< p > < b > If
you
notice
these
symptoms
then
you
need
to
take
action
to
prevent
further
damage. < / b > < / p >

< p > < b > What
you
need
to
do - eye
injuries < / b > < / p >
< hr >
< p > Tell
them
not to
rub
it as this
could
make
it
worse. < / p >

< p > < b > If
you
think
they
might
have
something in their
eye < / b > < / p >
< p > -Ask
them
to
sit
down
facing
a
light. < / p >
< p > -Gently
open
their
eyelids
with your thumbs and ask them to look right, left, up and down as you look closely at the eye.< / p >
< p > -If
you
can
see
something in there, wash
it
out
by
pouring
clean
water
over
the
inner
corner
of
the
eye. < / p >
< p > -If
this
doesn’t
work or the
eye
still
hurts, send or take
them
to
hospital. < / p >

< p > < b > If
you
think
their
eye
may
be
bruised or cut < / b > < / p >
< p > -Help
them
to
lie
on
their
back and hold
their
head
to
keep
it as still as possible. < / p >
< p > -Tell
them
to
keep
both
eyes
still, as moving
their
good
eye
will
also
move
the ‘bad’ eye, which
could
make
it
worse < / p >
< p > -Give
them
a
sterile
dressing, or a
clean
non - fluffy
pad
to
hold
over
their ‘bad’ eye. < / p >
< p > -If
it
will
be
a
while before you can get medical help, then you can hold the pad in place with a bandage.< / p >
< p > -Now
take or send
them
to
hospital. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div26" >

< img
src = "{% static '/IMAGES/snakebites.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Snakebites < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal26" >


Check
< / button >
< div


class ="modal fade" id="modal26" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Snakebites < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Most
North
American
snakes
aren
't dangerous to humans. Some exceptions include the rattlesnake, coral snake, water moccasin and copperhead. Their bites can be life-threatening.</p>

< p > If
you
are
bitten
by
a
venomous
snake, call
911 or your
local
emergency
number
immediately, especially if the
area
changes
color, begins
to
swell or is painful.Many
hospitals
stock
antivenom
drugs, which
may
help
you. < / p >

< p > < b > If
possible, take
these
steps
while waiting for medical help:< / b > < / p >
< p > -Remain
calm and move
beyond
the
snake
's striking distance.</p>
< p > -Remove
jewelry and tight
clothing
before
you
start
to
swell. < / p >
< p > -Position
yourself,
if possible, so that the bite is at or below the level of your heart.< / p >
< p > -Clean
the
wound, but
don
't flush it with water. Cover it with a clean, dry dressing.</p>

< p > < b > Caution < / b > < / p >
< hr >
< p > -Don
't use a tourniquet or apply ice.</p>
< p > -Don
't cut the wound or attempt to remove the venom.</p>
< p > -Don
't drink caffeine or alcohol, which could speed the rate at which your body absorbs venom.</p>
< p > -Don
't try to capture the snake. Try to remember its color and shape so that you can describe it, which will help in your treatment.</p>

< p > < b > Venomous
snakes in North
America < / b > < / p >
< hr >
< p > Of
the
venomous
snakes
found in North
America, all
but
the
coral
snake
have
slit - like
eyes and are
known as pit
vipers.Their
heads
are
triangular,
with a depression (pit) midway between the eye and nostril on either side of the head.< / p >

< p > Other
characteristics
are
unique
to
certain
venomous
snakes: < / p >

< p > -Rattlesnakes
rattle
by
shaking
the
rings
at
the
end
of
their
tails. < / p >
< p > -Water
moccasins
' mouths have a white, cottony lining.</p>
< p > -Coral
snakes
have
red, yellow and black
rings
along
the
length
of
their
bodies. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div27" >

< img
src = "{% static '/IMAGES/choking adult.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Choking
adults < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal27" >


Check
< / button >
< div


class ="modal fade" id="modal27" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Choking adults < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Choking is when
your
airway
gets
blocked and you
can’t
breathe
properly. < / p >

< p > When
someone
chokes, the
airway
can
either
be
partly or fully
blocked.If
it’s
a
mild
blockage, they
should
be
able
to
clear
it
themselves
by
coughing.If
it’s
a
severe
blockage, they
won’t
be
able
to
cough
so
without
anyone’s
help
they’ll
become
unresponsive. < / p >

< p > But if they
do
become
unresponsive, their
throat
muscles
could
relax and open
the
airway
enough
for you to give rescue breaths ‒ be prepared to give rescue breaths and chest compressions.< / p >

< p > < b > what
to
look
for < / b > < / p >
< hr >
< p > -If
you
think
someone is choking, ask
them: ‘Are
you
choking?’ to
check
they’re
not suffering
from something else.Can
they
speak, cry, cough or breathe? < / p >
< p > -If
they
can, they
should
be
able
to
clear
their
throat
on
their
own
by
coughing, so
encourage
them
to
cough. < / p >
< p > -If
they
can’t
cough or make
any
noise, it’s
serious. < / p >

< p > < b > what
you
need
to
do < / b > < / p >
< hr >
< p > < b > Step
1
of
4: Cough
it
out < / b > < / p >
< p > - Encourage
them
to
cough.If
this
doesn
't clear the obstruction, support their upper body with one hand and help them lean forward</p>

< p > < b > Step
2
of
4: Slap
it
out < / b > < / p >
< p > - If
coughing
doesn’t
work, help
the
casualty
bend
forward. < / p >
< p > - Use
the
heel
of
your
hand
to
give
up
to
five
sharp
back
blows
between
their
shoulder
blades. < / p >
< p > - Check
their
mouth
to
see if there’s
anything in there and,
if there is, get them to pick it out.< / p >

< p > < b > Step
3
of
4: Squeeze
it
out < / b > < / p >
< p > - If
back
blows
don’t
work, give
up
to
five
abdominal
thrusts. < / p >
< p > - Stand
behind
them. < / p >
< p > - Link
your
hands
between
their
tummy
button and the
bottom
of
their
chest,
with your lower hand clenched in a fist.< / p >
< p > - Pull
sharply
inwards and upwards. < / p >

< p > < b > Step
4
of
4: Call
for help< / b > < / p >
< p > - If
they’re
still
choking, call
999 or 112
for medical help. </ p >
< p > - Once
you’ve
called,
continue
steps
2 and 3 – back
blows and abdominal
thrusts – until
what’s in there
has
cleared, help
arrives or they
become
unresponsive. < / p >
< p > - If
they
become
unresponsive
at
any
stage, open
their
airway and check
their
breathing. < / p >
< p > - If
they’re
not breathing, start
chest
compressions and rescue
breaths(CPR - cardiopulmonary
resuscitation) to
try to release whatever’s stuck in there.Follow the instructions for treating someone who’s unresponsive and not breathing.< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div28" >

< img
src = "{% static '/IMAGES/scorpion bite.jpg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Scorpion
Bite < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal28" >


Check
< / button >
< div


class ="modal fade" id="modal28" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Scorpion Bite < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Risk
Factors
For
Scorpion
Bite < / b > < / p >
< hr >
< p > There
are
certain
factors
which
increase
the
risk
of
you
getting
a
scorpion
bite: < / p >
< p > -Scorpions
are
found in desert
regions, and are
active in summer and spring. < / p >
< p > -Scorpions, especially
bark
scorpions;
hide in the
bark
of
the
trees and beneath
the
rocks and logs. < / p >
< p > -In
household
scenario, scorpions
hide in trash
cans, in firewood, bedding and shoes. < / p >
< p > -You
are
more
likely
to
encounter
poisonous
scorpions
when
traveling
to
developing
countries.They
can
also
hide in your
clothing and luggage and come
home
with you. </ p >

< p > < b > Symptoms
Produced
From
Scorpion
Bite < / b > < / p >
< hr >
< p > Most
of
the
times, a
scorpion
sting
causes
discomfort
which
gradually
abates.Sometimes, a
person
can
feel
moderate
to
severe
discomfort / pain, which
can
be
described as the
following: < / p >

< p > -Patient
experiences
a
painful, burning, tingling, numbing
sensation
at
site
of
the
scorpion
sting. < / p >
< p > -There is slight
redness
seen
at
the
scorpion
sting
site. < / p >
< p > -Just
like
bee
sting, patient
can
also
develop
an
allergic
reaction
to
a
scorpion
sting, which
can
sometimes
be
life
threatening(anaphylaxis). < / p >

< p > Sometimes
a
person
can
experience
a
severe
reaction or develop
serious
symptoms
sue
to
scorpion
bite or scorpion
sting, which
comprise
of: < / p >

< p > -Numbness
all
over
the
body. < / p >
< p > -Difficulty in swallowing(dysphagia). < / p >
< p > -Tongue
thickness. < / p >
< p > -Blurry
vision. < / p >
< p > -Erratic
eye
movements. < / p >
< p > -Excessive
salivation. < / p >
< p > -Seizures. < / p >
< p > -Vomiting. < / p >
< p > -Difficulty in breathing. < / p >
< p > -Excessive
sweating. < / p >
< p > -Tachycardia. < / p >
< p > -Hypertension / hypotension. < / p >

< p > All
these
symptoms
of
scorpion
bite
are
serious and life
threatening and need
prompt
medical
attention. < / p >

< p > < b > Home
Remedies
And
First
Aid
For
Scorpion
Bite < / b > < / p >
< hr >
< p > Home
treatment is usually
sufficient
for most of the scorpion sting and it comprises of:< / p >

< p > -Wash
the
scorpion
sting
site
with soap and water. </ p >
< p > -Remove
any
jewelry
worn
at
the
scorpion
bite
site, as swelling in the
site
region
will
hamper
the
circulation. < / p >
< p > -Application
of
ice or cool
compresses
should
be
done
for at least 10 minutes.Remove the cold compresses for 10 minutes then apply again.This will help in easing the pain, burning sensation and swelling sue to scorpion bite.< / p >
< p > -Keep
the
affected
region
above
the
level
of
the
heart. < / p >
< p > -In
case if the
patient is having
difficulty
swallowing, avoid
consuming
any
food or drinks. < / p >
< p > -Keep
the
patient as still and calm as possible, this
will
slow
down
the
spreading
of
the
poison. < / p >
< p > -OTC
analgesics, such as acetaminophen(Tylenol)
can
be
taken
every
4
hours
for pain relief of scorpion bite.NSAIDs, such as ibuprofen and aspirin should be avoided as they can cause other problems.< / p >
< p > -If
there is secondary
infection in the
scorpion
sting
site, then
antibiotics
are
given. < / p >
< p > -Do
not make
a
cut in the
wound and avoid
applying
suction
to
it. < / p >
< p > -Home
Remedy
For
Scorpion
Bite
Using
Turmeric: Turmeric
has
anti
inflammatory, antibiotic and healing
property
which
makes
it
a
great
first
aid
for scorpion bites / stings.It acts as an antidote as well.One can sprinkle some amount of turmeric on the scorpion bite / sting area or can make a paste of turmeric with water and apply over the wound.< / p >
< p > -Onion
Juice is an
effective
home
remedy
for Scorpion Bite.Onion has anti-inflammatory and antibiotic properties.Applying onion juice on the scorpion bite site can be helpful first aid.< / p >

< p > < b > What
To
Do
If
Stung
By
A
Bark
Scorpion? < / b > < / p >
< hr >
< p > If
the
patient is having
serious
symptoms
after
a
scorpion
bite, which
are
mentioned
above, especially if the
victim is an
infant, a
child or someone
elderly, then
the
following
steps
should
be
taken: < / p >

< p > -Immediately
call
emergency
care. < / p >
< p > -Continuous
application
of
ice and cool
compresses
should
be
done
at
the
scorpion
sting
site. < / p >
< p > -Keep
the
patient as still and calm as possible, this
will
slow
down
the
spreading
of
the
poison. < / p >
< p > -If
possible, carefully
collect
the
injured / dead
scorpion in a
sealed
container.This
can
be
shown
to
the
physician and can
be
helpful in treatment. < / p >
< p > -Anti - venom
therapy is available
for sting by a bark scorpion (Centruroides species).The anti-venom helps in stopping all the symptoms in about 4 hours after it's given.</p>
< p > -All, except the
mildest
symptoms, need
hospital
admission and observation
for 24 hours. </ p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div29" >

< img
src = "{% static '/IMAGES/bee.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Bee and Wasp
Stings < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal29" >


Check
< / button >
< div


class ="modal fade" id="modal29" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Bee and Wasp Stings < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Treating
bee and wasp
stings
depends
on
their
severity.The
majority
of
problems
that
require
medical
attention
come
from an allergic

reaction
to
the
sting.In
most
cases, complications
from that reaction

respond
well
to
medications - - when
given in time. < / p >

< p > < b > Home
Treatment
for Bee and Wasp Stings < / b > < / p >
< hr >
< p > Most
insect
stings
for someone who is not allergic need no more than first aid given at home.Then you can avoid further stings by wearing protective clothing, using insect repellent, and staying out of infested areas.< / p >
< p > Here
are
the
steps
you
need
to
take
after
someone
who is allergic
has
been
stung: < / p >

< p > -Remove
any
stingers
immediately.Some
experts
recommend
scraping
out
the
stinger
with a credit card.< / p >
< p > -Applying
ice
to
the
site
may
provide
some
mild
relief.Apply
ice
for 20 minutes once every hour as needed.Wrap the ice in a towel or keep a cloth between the ice and skin to keep from freezing the skin.< / p >
< p > -Taking
an
antihistamine
such as diphenhydramine(Benadryl) or a
nonsedating
one
such as loratadine(Claritin)
will
help
with itching and swelling. </ p >
< p > -Take
ibuprofen(Motrin) or acetaminophen(Tylenol)
for pain relief as needed.< / p >
< p > -Wash
the
sting
site
with soap and water.Placing hydrocortisone cream on the sting can help relieve redness, itching, and swelling.< / p >
< p > -If
it
's been more than 10 years since your last tetanus booster, get a booster within the next few days.</p>
< p > -Most
insect
stings
require
no
additional
medical
care. < / p >

< p > If
you
know
you
may
be
allergic, especially if you
've had a severe reaction in the past when stung by a bee or wasp, seek immediate medical help. Take an antihistamine such as diphenhydramine (Benadryl) or a nonsedating one such as loratadine (Claritin) as soon as possible. If you have been prescribed epinephrine (EpiPen) for an allergic reaction, always carry two with you and use it as directed.</p>

< p > < b > Medical
Treatment
for Bee and Wasp Stings < / b > < / p >
< hr >
< p > If
you
have
a
single
sting
with no allergic symptoms, you may require only local wound care such as cleaning and applying antibiotic ointment.Any stingers that remain will be removed.And you may be given an oral antihistamine to treat itching.The doctor may also tell you to use ibuprofen (Motrin) or acetaminophen (Tylenol) for pain.If your tetanus immunization is not current, you'll receive a booster shot.</p>

< p > With
mild
allergic
symptoms
such as a
rash and itching
over
your
body
but
no
problems
with breathing or other vital signs, you may be treated with an antihistamine.You may also be given steroids.In some cases, the doctor will give you an epinephrine (adrenaline) injection.Treatment may be started at the scene or in the ambulance by the emergency medics.If you are doing well, you may be sent home after observation in the emergency department.< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div30" >

< img
src = "{% static '/IMAGES/jellyfish.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Jellyfish
Sting < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal30" >


Check
< / button >
< div


class ="modal fade" id="modal30" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Jellyfish Sting < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Call
emergency < / b > < / p >
< hr >
< p > - The
person
displays
signs
of
a
severe
allergic
reaction. < / p >
< p > - The
sting is
from a box

jellyfish. < / p >
< p > - The
sting
covers
more
than
half
an
arm or leg. < / p >

< p > < b > First
Aid < / b > < / p >
< hr >
< p > 1.
Get
the
Person
Out
of
the
Water < / p >
< p > 2.
Stop
the
Stinging < / p >
< p > - Wash
the
area
with seawater to deactivate stinging cells.Or you can remove tentacles by scraping with a credit card or other plastic object.< / p >
< p > - For
a
sting in tropical
waters - - especially
from the Hawaiian

box
jellyfish or a
Portuguese
man - of - war: < / p >
< p > - After
removing
the
tentacles, immerse
the
affected
arm or leg
immediately in hot
water
at
40
to
45°C(104
to
113°F) for at least twenty minutes.A hot shower can be used instead for other parts of the body.< / p >
< p > - Anti - venom is available
for severe Australian box jellyfish stings.It should be given right away to be most effective.< / p >

< p > 3.
Decontaminate and Remove
Tentacles < / p >
< p > For
jellyfish
stings, the
American
Heart
Association
recommends
the
following: < / p >

< p > - Rinse
the
area
with vinegar for at least 30 seconds.If vinegar is not available, a solution of baking soda can be used.This will help deactivate the stinging cells.< / p >
< p > - Next, soak
the
area in hot
water
for at least 20 minutes if possible.Cold packs can be used instead if the area can’t be soaked in hot water.< / p >

< p > These
treatments
are
based
on
research
done in the
Indo - Pacific
areas, however, and may
not be
effective in the
oceans
of
the
North
Atlantic.In
fact, in this
area, vinegar
may
actually
make
the
symptoms
worse, depending
on
the
type
of
jellyfish.Some
experts
therefore
recommend
removing
the
stinging
cells and rinsing in seawater. < / p >

< p > 4.
Treat
Discomfort < / p >
< p > Use
mild
hydrocortisone
cream or oral
antihistamine
to
help
relieve
itching and swelling. < / p >

< p > 5.
Follow
Up < / p >
< p > For
less
severe
sting: < / p >

< p > - Use
ice
packs or over - the - counter
pain
relievers
for welts.< / p >
< p > - Clean
open
sores
3
times
a
day and apply
antibiotic
ointment.Bandage if needed. < / p >

< p > For
a
severe
reaction: < / p >

< p > - The
person
may
be
hospitalized
for several days. </ p >
< p > - Anti - venom
may
be
administered
for box jellyfish stings.< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div31" >

< img
src = "{% static '/IMAGES/animal bite.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Animal
Bites
Treatment < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal31" >


Check
< / button >
< div


class ="modal fade" id="modal31" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Animal Bites Treatment < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Call
emergency if: < / b > < / p >
< hr >
< p > - The
person
has
been
seriously
wounded. < / p >
< p > - Bleeding
can
't be stopped after 10 minutes of firm and steady pressure.</p>
< p > - Bleeding is severe. < / p >
< p > - Blood
spurts
from the wound.< / p >

< p > < b > First
Aid < / b > < / p >
< hr >
< p > 1.
Stop
Bleeding < / p >
< p > Apply
direct
pressure
until
bleeding
stops. < / p >

< p > 2.
Clean and Protect < / p >
< p > For
a
wound or superficial
scratch
from an animal

bite: < / p >

< p > - Gently
clean
with soap and warm water.Rinse for several minutes after cleaning.< / p >
< p > - Apply
antibiotic
cream
to
reduce
risk
of
infection, and cover
with a sterile bandage.< / p >

< p > 3.
Get
Help < / p >
< p > - Get
medical
help
immediately
for any animal bite that is more than a superficial scratch or if the animal was a wild animal or stray, regardless of the severity of the injury.< / p >
< p > - If
the
animal
's owner is available, find out if the animal'
s
rabies
shots
are
up - to - date.Give
this
information
to
your
health
care
provider. < / p >
< p > - If
the
animal
was
a
stray or wild
animal, call
the
local
health
department or animal
control
immediately. < / p >

< p > 4.
Follow
Up < / p >
< p > - The
health
care
provider
will
make
sure
the
wound is thoroughly
clean and may
prescribe
antibiotics. < / p >
< p > - The
health
care
provider
may
numb
the
wound and look
for any deeper damage.< / p >
< p > - If
there is any
risk
of
rabies
infection, the
health
care
provider
will
recommend
anti - rabies
treatment. < / p >
< p > - The
person
may
require
stitches, depending
on
how
big
the
wound is and where
it is located. < / p >
< p > - The
person
may
also
require
a
tetanus
shot or booster. < / p >
< p > - The
health
care
provider
may
recommend
ibuprofen or acetaminophen
for pain.< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div32" >

< img
src = "{% static '/IMAGES/fractures.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Broken
bones and fractures < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal32" >


Check
< / button >
< div


class ="modal fade" id="modal32" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Broken bones and fractures < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > A
break or crack in a
bone is called
a
fracture. < / p >

< p > In
most
cases
the
damage
to
the
bone
will
be
under
the
skin, which is called
a
closed
fracture, but
sometimes
bits
of
the
bone
can
puncture
through
the
skin
to
become
an
open
fracture. < / p >

< p > In
both
cases
you
'll need to treat the casualty for shock. Even if you can'
t
see
any
blood, the
break
might
have
caused
some
internal
bleeding. < / p >

< p > To
break
a
fully
grown
bone, a
huge
amount
of
force is needed.But
bones
that
are
still
growing
are
supple and can
split, crack or bend
quite
easily, a
bit
like
a
twig. < / p >

< p > < b > What
to
look
for < / b > < / p >
< hr >
< p > < b > The
seven
things
to
look
for are: < / b > < / p >
< p > 1.
Swelling < / p >
< p > 2.
Difficulty
moving < / p >
< p > 3.
Movement in an
unnatural
direction < / p >
< p > 4.
A
limb
that
looks
shorter, twisted or bent < / p >
< p > 5.
A
grating
noise or feeling < / p >
< p > 6.
Loss
of
strength < / p >
< p > 7.
Shock < / p >

< p > < b > What
you
need
to
do - Broken
bones and fractures < / b > < / p >
< hr >
< p > - If
it is an
open
fracture, cover
the
wound
with a sterile dressing and secure it with a bandage.Apply pressure around the wound to control any bleeding.< / p >
< p > - Support
the
injured
body
part
to
stop
it
from moving.This should

ease
any
pain and prevent
any
further
damage. < / p >
< p > - Once
you’ve
done
this, call
999 or 112
for medical help.While waiting for help to arrive, don’t move them unless they’re in immediate danger.< / p >

< p > < b > Waiting
for medical help to arrive < / b > < / p >
< hr >
< p > Protect
the
injured
area
by
using
bandages
to
secure
it
to
an
uninjured
part
of
the
body
to
stop
it
from moving.For example, fractures

on
the
arm
can
be
secured
with a sling, and a leg with a fracture can be tied to the uninjured leg.< / p >

< p > Keep
checking
the
casualty
for signs of shock.This does not mean emotional shock, but is a life-threatening condition, often caused by losing blood.< / p >

< p > If
they
lose
responsiveness
at
any
point, open
their
airway, check
their
breathing and prepare
to
treat
someone
who’s
become
unresponsive. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div33" >

< img
src = "{% static '/IMAGES/epilepsy.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Epilepsy < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal33" >


Check
< / button >
< div


class ="modal fade" id="modal33" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Epilepsy < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Below is a
basic
guide
about
what
to
do in case
of
a
seizure. < / p >

< p > Convulsive
seizures
where
the
body
stiffens(tonic
phase) followed
by
general
muscle
jerking(clonic
phase).< / p >

< p > < b > DO < / b > < / p >
< hr >
< p > -Remain
calm < / p >
< p > -Stay
with person </ p >
< p > -Time
seizure < / p >
< p > -Protect
from injury especially

the
head < / p >
< p > -Roll
into
recovery
position
after
jerking
stops
OR
immediately if food / fluid / vomit in mouth < / p >
< p > -Maintain
privacy and dignity < / p >
< p > -Observe and monitor
breathing < / p >
< p > -Gently
reassure
until
recovered < / p >

< p > < b > DO
NOT < / b > < / p >
< hr >
< p > -Put
anything in their
mouth < / p >
< p > -Restrain
the
person < / p >
< p > -Move
person
unless in danger < / p >
< p > -Apply
CPR < / p >

< p > < b > If
seizure
occurs in wheelchair, car
seat or stroller: < / b > < / p >
< hr >
< p > -Leave
person in chair
with seatbelt on < / p >
< p > -Lean
person
slightly
to
one
side
to
aid
drainage
of
any
fluid / food / vomit in mouth < / p >
< p > -Support
head and protect
airway as required < / p >
< p > -After
jerking
stops
carefully
remove
from chair and place in recovery
position if possible or required < / p >

< p > < b > Call
an
ambulance if: < / b > < / p >
< hr >
< p > -You
are in any
doubt < / p >
< p > -You
arrive
after
the
seizure
has
started < / p >
< p > -Injury
has
occurred < / p >
< p > -Food or water is in mouth
during
seizure < / p >
< p > -The
seizure
has
occured in water < / p >
< p > -The
seizure
lasts
longer
than
normal
for that person </ p >
< p > -The
seizure
lasts
longer
than
five
minutes < / p >
< p > -Another
seizure
follows
quickly < / p >
< p > -The
person is non - responsive
for more than 5 minutes after the seizure ends < / p >
< p > -The
person
has
breathing
difficulties
after
the
jerking
stops < / p >
< p > -It is the
person’s
first
known
seizure < / p >
< p > -This is not an
exhaustive
list, however
it is a
starting
point
to
help
you
consider
response
to
seizures. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div34" >

< img
src = "{% static '/IMAGES/asthma.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Asthma < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal34" >


Check
< / button >
< div


class ="modal fade" id="modal34" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Asthma < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Asthma and hayfever < / b > < / p >
< hr >
< p > Hayfever is a
major
risk
factor
for asthma, and the two are often experienced side by side.Poorly treated hayfever can increase the threat of an asthma attack.< / p >

< p > We
recommend
regularly
checking
pollen
counts and staying
on
top
of
medication
to
keep
asthma
attacks
at
bay.If
you’re
asthmatic and you
know
hay
fever
affects
you, keep
your
inhaler
with you at all times.< / p >

< p > < b > Recognise
an
asthma
attack < / b > < / p >
< hr >
< p > < b > What is an
asthma
attack? < / b > An
asthma
attack is when
lung
muscles
spasm and the
airway
swells, becoming
narrow and making
it
hard
to
breathe. < b > What
causes
an
asthma
attack? < / b > These
attacks
are
caused
by
many
things
including
allergies, smoke or exercise. < / p >

< p > < b > How
to
recognise
an
asthma
attack: < / b > < / p >
< p > -Difficulty
breathing < / p >
< p > -Wheezing
on
the
exhale < / p >
< p > -Difficulty
speaking and whispering < / p >
< p > -Distress and anxiety < / p >
< p > -Coughing < / p >
< p > -Grey - blue
tinge
to
the
lips, earlobes and nailbeds < / p >

< p > < b > -Know
what
to
do < / b > < / p >
< hr >
< p > -Knowing
first
aid
can
help
those
around
you
stay
safe.Here’s
what
you
need
to
know if some is having
an
asthma
attack: < / p >

< p > -Keep
calm: panicking
could
make
their
breathing
worse.Encourage
slow, deep
breaths < / p >
< p > -Help
them
into
a
comfortable
breathing
position, and encourage
them
to
use
an
inhaler if they
have
one < / p >
< p > -A
mild
attack
should
ease
within
a
few
minutes
of
using
an
inhaler.If
it
doesn’t, encourage
them
to
take
one or two
puffs
every
two
minutes, up
to
a
maximum
of
10
puffs < / p >
< p > -Monitor
their
vital
signs: breathing, pulse and responsiveness < / p >
< p > -Call
an
ambulance if the
inhaler
has
no
effect, or the
person is becoming
exhausted < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div35" >

< img
src = "{% static '/IMAGES/sprains.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Strains and sprains < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal35" >


Check
< / button >
< div


class ="modal fade" id="modal35" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Strains and sprains < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Introduction < / b > < / p >
< hr >
< p > Strains and sprains
are
common
injuries
which
affect
the
soft
tissues
around
joints – the
muscles, tendons and ligaments. < / p >

< p > They
happen
when
the
tissues
are
stretched, twisted or torn
by
violent or sudden
movements,
for instance if someone changes direction suddenly, or falls and lands awkwardly.< / p >

< p > A
sprain is when
a
ligament
has
been
twisted or torn. < / p >

< p > A
strain is when
the
muscle
has
been
overstretched and has
partially
torn.(A
rupture is when
a
muscle or tendon is completely
torn).< / p >

< p > < b > What
to
look
for < / b > < / p >
< p > If
you
think
someone
may
have
strained or sprained
a
muscle, ligament or tendon, these
are
the
three
key
things
to
look
for: < / p >

< p > -Pain and tenderness < / p >
< p > -Difficulty
moving < / p >
< p > -Swelling and bruising < / p >

< p > < b > What
you
need
to
do < / b > < / p >
< hr >
< p > Remember
RICE
for the four steps to deal with strains and sprains:< / p >
< p > -Rest < / p >
< p > -Ice < / p >
< p > -Comfortable
support < / p >
< p > -Elevation < / p >

< p > < b > Treatment
for strains and sprains < / b > < / p >
< hr >
< p > -Step
1
of
4: Rest < / p >
< p > Help
them
to
sit or lie
down and support in a
comfortable
raised
position
the
part
they’ve
hurt. < / p >

< p > -Step
2
of
4: Ice < / p >
< p > To
cool
the
area, apply
a
cold
compress, like
an
ice
pack or cold
pad.This
will
help
to
reduce
the
swelling, bruising and pain.Do
not leave
on
for more than ten minutes.< / p >

< p > -Step
3
of
4: Comfortable
support < / p >
< p > Leave
the
cold
compress in place or wrap
a
soft
layer
of
padding, e.g.cotton
wool, around
the
area.Tie
a
support
bandage
around
it, to
hold
it in place, which
goes
up as far as the
next
joint
on
each
side.For
example,
for an ankle injury, the bandages should go from the base of the toes to the knees.< / p >

< p > -Step
4
of
4: Elevation < / p >
< p > -Elevate
the
injury and support
it
with something soft, like cushions.< / p >
< p > -If
the
pain is severe, or they
can’t
use
their
limb
at
all, take or send
them
to
hospital.Otherwise, just
tell
them
to
rest
it and to
see
a
health
care
professional,
if necessary. </ p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div36" >

< img
src = "{% static '/IMAGES/stuck ring.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Removing
a
Stuck
Ring < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal36" >


Check
< / button >
< div


class ="modal fade" id="modal36" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Removing a Stuck Ring < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > First
Aid < / b > < / p >
< hr >
< p > -Insert
the
end
of
a
thin
thread or dental
floss
down
the
ring < / p >
< p > -Use
cream or oil
to
grease
the
thread and the
ring
finger < / p >
< p > -Pull
the
other
end
of
the
string and wrapped
it
tightly
around
the
finger, and make
sure
that
the
thread
has
been
wrapped
regularly and smoothly
until
the
bottom
of
the
finger
joint. < / p >
< p > -Catch
the
end
of
the
string
that
was
entered
under
the
ring, and start
release
thread in the
same
direction(ring
should
moving
up
the
thread).< / p >

< p > < b > If
there is swelling or if it is not possible
to
take
out
the
ring, release
the
thread and go
to
the
emergency
department
of
the
nearest
hospital
so
that
they
could
cut
the
ring. < / b > < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div37" >

< img
src = "/IMAGES/fishhook.jpg"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Fishhook
Removal < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal37" >


Check
< / button >
< div


class ="modal fade" id="modal37" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Fishhook Removal < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > First
Aid < / b > < / p >
< hr >
< p > Fishing is a
widespread
leisurely
activity
that
rarely
results in an
emergency.However, trauma
from a fishhook

piercing
the
skin is fairly
common.Use
the
following
guidelines
to
remove
a
fishhook: < / p >

< p > -Use
pliers or forceps
to
push
the
hook
gently
through
the
skin, following
the
curve
of
the
hook. < / p >
< p > -Cut
off
the
barb
so
that
the
unbarbed
portion
of
the
fishhook
can
be
backed
out. < / p >
< p > -Do
not close
the
wound. < / p >
< p > -Follow
wound
care
guidelines, especially
checking
on
tetanus
vaccine
status. < / p >
< p > -Start
antibiotics
immediately. < / p >

< p > < b > When
to
Seek
Medical
Care < / b > < / p >
< hr >
< p > A
fishhook
wound
can
lead
to
a
serious
infection, so
be
certain
to
consult
a
doctor
about
available
medications
for the treatment of fishhook wounds.People who experience a fishhook puncture should be immunized for tetanus if more than 5 years have passed since their last inoculation.Continue Reading < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div38" >

< img
src = "{% static '/IMAGES/nuts.jpg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Testicle
Injuries < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal38" >


Check
< / button >
< div


class ="modal fade" id="modal38" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Testicle Injuries < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > First
Aid < / b > < / p >
< hr >
< p > -Calm and reassure
the
casualty. < / p >
< p > -Apply
an
ice
pack or cold
compress
to
the
skin
of
the
testicle
to
lessen
swelling.Direct
contact
between
the
ice and scrotum
should
be
avoided. < / p >
< p > -Assuming
that
the
casualty
has
no
allergic
reaction, pain
killers
may
be
given
to
reduce
pain. < / p >
< p > -Raise
the
scrotum and observe
for pain relief.If there is, try wearing tight briefs which can help raise the testicles.< / p >

< p > < b > Things
to
remember < / b > < / p >
< hr >
< p > -If
you
injure
your
testicles(during
sport,
for example), always seek urgent medical advice.< / p >
< p > -Perform
testicular
self - examination(TSE)
regularly. < / p >
< p > -See
your
doctor if you
experience
any
pain or unusual
symptoms, or if you find a lump or swelling.< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div39" >

< img
src = "{% static '/IMAGES/labour.jpg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Labor
Signs < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal39" >


Check
< / button >
< div


class ="modal fade" id="modal39" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Labor Signs < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Call
Emergency if: < / b > < / p >
< hr >
< p > -The
woman
has
heavy
vaginal
bleeding. < / p >
< p > -The
woman
has
severe
stomach or pelvic
pain. < / p >
< p > -The
woman
has
a
seizure. < / p >
< p > -The
woman
loses
consciousness. < / p >
< p > -The
umbilical
cord is bulging
into
the
vagina
with gushing or leaking fluid.< / p >

< p > < b > Look
for Signs of Labor < / b > < / p >
< p > Signs
that
labor
has
begun
include: < / p >
< p > -Contractions
that
come
at
regular
intervals, increase in frequency, do
not stop
when
the
woman
changes
position or relaxes, and may
cause
pelvic
pressure and discomfort or dull
ache in the
back or lower
abdomen < / p >
< p > -A
sudden
gush or a
steady
trickle
of
fluid
when
the
amniotic
membrane
ruptures("water breaks") < / p >
< p > -Pink or slightly
bloody
mucus
discharged
into
the
vagina < / p >
< p > -The
fetus
lowers
into
the
pelvis, which
may
cause
more
frequent
urination < / p >

< p > < b > When
to
Call
a
Health
Care
Provider < / b > < / p >
< hr >
< p > Call
the
health
care
provider
right
away if: < / p >
< p > -In
first
pregnancy, contractions
are
very
uncomfortable and coming
every
5
minutes
for 1 hour.This timing, however, may vary.Ask your health care provider what they recommend.< / p >
< p > -In
subsequent
pregnancies, contractions
are
coming
every
7
to
10
minutes
for an hour.This timing, however, may vary.Ask your health care provider what they recommend.< / p >
< p > -The
woman
's "water breaks," even without contractions. She should avoid baths, douching, tampons, or sexual intercourse.</p>
< p > -The
woman
has
vaginal
bleeding(more
than
spotting).< / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div40" >

< img
src = "{% static '/IMAGES/stomachpain.jpg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Abdominal
Pain < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal40" >


Check
< / button >
< div


class ="modal fade" id="modal40" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Abdominal Pain < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Treat
Symptoms < / b > < / p >
< hr >
< p > -For
heartburn
from gastroesophageal reflux

disease(GERD), take
an
over - the - counter
antacid or acid
reducer. < / p >
< p > -For
constipation, take
a
mild
stool
softener or laxative. < / p >
< p > -For
pain, take
acetaminophen(Aspirin
Free
Anacin, Liquiprin, Panadol, Tylenol).Avoid
NSAIDs
such as aspirin, ibuprofen(Advil, Midol, Motrin), or naproxen(Naprosyn, Aleve, Anaprox, Naprelan), because
they
can
cause
stomach
irritation or bleeding. < / p >

< p > < b > When
to
Call
a
Doctor < / b > < / p >
< hr >
< p > Seek
medical
help if the
person: < / p >
< p > -Has
severe
abdominal
pain or pain
that
lasts
several
days < / p >
< p > -Has
nausea, fever, or inability
to
keep
food
down
for several days </ p >
< p > -Has
bloody
stools < / p >
< p > -Has
painful
urination < / p >
< p > -Has
blood in the
urine < / p >
< p > -Cannot
pass
stools, especially if also
vomiting < / p >
< p > -Has
difficulty
breathing < / p >
< p > -Had
an
injury
to
the
abdomen in the
days
before
the
pain
started < / p >
< p > -Has
heartburn
that
isn
't relieved by over-the-counter drugs or last longer than two weeks</p>

< p > < b > Call
emergency if: < / b > < / p >
< hr >
< p > -Vomits
blood < / p >
< p > -Has
severe
difficulty
breathing < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div41" >

< img
src = "{% static '/IMAGES/wound.jpeg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Bleeding
Cuts or Wounds < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal41" >


Check
< / button >
< div


class ="modal fade" id="modal41" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Bleeding Cuts or Wounds < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > Call
emergency if: < / b > < / p >
< hr >
< p > -Bleeding is severe < / p >
< p > -You
suspect
internal
bleeding < / p >
< p > -There is an
abdominal or chest
wound < / p >
< p > -Bleeding
can
't be stopped after 10 minutes of firm and steady pressure</p>
< p > -Blood
spurts
out
of
wound < / p >

< p > < b > 1.
Stop
Bleeding < / b > < / p >
< hr >
< p > -Apply
direct
pressure
on
the
cut or wound
with a clean cloth, tissue, or piece of gauze until bleeding stops.< / p >
< p > -If
blood
soaks
through
the
material, don’t
remove
it.Put
more
cloth or gauze
on
top
of
it and
continue
to
apply
pressure. < / p >
< p > -If
the
wound is on
the
arm or leg,
raise limb
above
the
heart,
if possible, to help slow bleeding.< / p >
< p > -Wash
your
hands
again
after
giving
first
aid and before
cleaning and dressing
the
wound. < / p >
< p > -Do
not apply
a
tourniquet
unless
the
bleeding is severe and not stopped
with direct pressure.< / p >

< p > < b > 2.
Clean
Cut or Wound < / b > < / p >
< hr >
< p > -Gently
clean
with soap and warm water.Try to rinse soap out of wound to prevent irritation.< / p >
< p > -Don’t
use
hydrogen
peroxide or iodine, which
can
damage
tissue. < / p >

< p > < b > 3.
Protect
the
Wound < / b > < / p >
< hr >
< p > -Apply
antibiotic
cream
to
reduce
risk
of
infection and cover
with a sterile bandage.< / p >
< p > -Change
the
bandage
daily
to
keep
the
wound
clean and dry. < / p >

< p > < b > 4.
When
to
Call
a
Doctor < / b > < / p >
< hr >
< p > -The
wound is deep or the
edges
are
jagged or gaping
open. < / p >
< p > -The
wound is on
the
person’s
face. < / p >
< p > -The
wound
has
dirt or debris
that
won’t
come
out. < / p >
< p > -The
wound
shows
signs
of
infection, such as redness, tenderness, or a
thick
discharge, or if the person runs a fever.< / p >
< p > -The
area
around
the
wound
feels
numb. < / p >
< p > -Red
streaks
form
around
the
wound. < / p >
< p > -The
person
has
a
puncture
wound or deep
cut and hasn’t
had
a
tetanus
shot in the
past
five
years, or anyone
who
hasn’t
had
a
tetanus
shot in the
past
10
years. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="div42" >

< img
src = "{% static '/IMAGES/hiccups.jpg' %}"
width = "100"
height = "80" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Hiccups
Treatment < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal42" >


Check
< / button >
< div


class ="modal fade" id="modal42" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < p > < b > Hiccups Treatment < / b > < / p > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > < b > 1.
Try
Home
Remedies < / b > < / p >
< hr >
< p > -Hold
your
breath. < / p >
< p > -Drink
a
glass
of
water
quickly. < / p >
< p > -Put
a
teaspoon
of
sugar
on
the
tongue and let
it
slowly
dissolve.For
a
young
child, use
corn
syrup. < / p >
< p > -Pull
on
the
tongue. < / p >
< p > -Gargle
water. < / p >
< p > -Use
smelling
salts. < / p >

< p > < b > 2.
When
to
See
a
Health
Care
Provider < / b > < / p >
< hr >
< p > -See
a
health
care
provider if the
hiccups
last
more
than
3
hours and are
severe
enough
to
interfere
with eating, breathing, or sleeping.< / p >
< p > -See
a
doctor
quickly if severe
stomach
pain, fever, shortness
of
breath, vomiting, throat
tightness, weight
loss, or coughing
up
blood
accompany
hiccups. < / p >
< / div >
< div


class ="modal-footer" >

< button
type = "button"


class ="btn btn-secondary" data-dismiss="modal" > Close < / button >

< / div >
< / div >
< / div >
< / div >
< / div >
< / main >

< !-- Optional
JavaScript -->
< !-- jQuery
first, then
Popper.js, then
Bootstrap
JS -->
< script
src = "https://code.jquery.com/jquery-3.3.1.slim.min.js"
integrity = "sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
crossorigin = "anonymous" > < / script >
< script
src = "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
integrity = "sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
crossorigin = "anonymous" > < / script >
< script
src = "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
integrity = "sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
crossorigin = "anonymous" > < / script >
< / body >
< / html >