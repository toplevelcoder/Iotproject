< !DOCTYPE
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
charset = "utf-8" / >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1, shrink-to-fit=no"
/ >
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
href = "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
integrity = "sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
crossorigin = "anonymous"
/ >
< link
rel = "stylesheet"
href = "{% static 'CSS/first_aid_gloss.css' %}" / >
< title > INFORMATION < / title >
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
data - toggle = "collapse"
data - target = "#navbarSupportedContent"
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
< div >
< img


class ="w-100 p-100" src="{% static '/IMAGES/info.jpg' %}" height="500" alt="" / >

< / div >
< div


class ="btn-group btn-group-toggle vertical-center" >

< a
href = "{%url 'first_aid_info'%}"


class ="btn btn-outline-dark " > General < / a >

< a
href = "{%url 'first_aid_gloss'%}"


class ="btn btn-outline-dark" style="padding-right: 23px;" > Gloss < / a >

< / div >
< main >
< div


class ="div1" >

< img
src = "{% static '/IMAGES/abrasion.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Abrasion < / span >
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


class ="modal-title" id="exampleModalLongTitle" > < b > Abrasion < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > Medical
term
for a graze to the skin.An abrasion is damage to the superficial layers to the skin.< / p >
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
src = "{% static '/IMAGES/adrenaline.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Adrenaline < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal2" >


Check
< / button >
< div


class ="modal fade" id="modal2" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Adrenaline < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
hormone
released
by
the
adrenal
glands(just
above
the
kidneys).It
increases
the
heart
rate and causes
blood
vessels
to
constrict.This
hormone is responsible
for the 'fight or flight' response.< / p >
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
src = "{% static '/IMAGES/anaphylaxis.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Anaphylaxis < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal3" >


Check
< / button >
< div


class ="modal fade" id="modal3" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Anaphylaxis < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
life - threatening
whole
body
allergic
reaction
which
causes
airway
swelling and shock. < / p >
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
src = "{% static '/IMAGES/angina.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Angina < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal4" >


Check
< / button >
< div


class ="modal fade" id="modal4" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Angina < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > Chest
pain
brought
on
by
physical
exertion or anxiety
due
to
narrowing
of
the
arteries in the
heart.Often
relieved
with rest and medication. </ p >
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
src = "{% static '/IMAGES/aspirin.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Aspirin < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal5" >


Check
< / button >
< div


class ="modal fade" id="modal5" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Aspirin < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
drug
that
slows
down
the
clotting
of
the
blood. < / p >
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
src = "{% static '/IMAGES/asthma.jpeg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Asthma < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal6" >


Check
< / button >
< div


class ="modal fade" id="modal6" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Asthma < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
medical
condition
characterised
by
difficulty in breathing
caused
by
constriction
of
the
small
air
tubes in the
lungs. < / p >
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
src = "{% static '/IMAGES/defibrillator.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Automated
External
Defibrillator < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal7" >


Check
< / button >
< div


class ="modal fade" id="modal7" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Automated External Defibrillator < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
device
that
delivers
a
controlled
electrical
shock
to
the
heart in order
to
restore
its
normal
rhythm. < / p >
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
src = "{% static '/IMAGES/c.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
C - spine < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal8" >


Check
< / button >
< div


class ="modal fade" id="modal8" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > C-spine < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > Cervical
spine - your
neck. < / p >
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
src = "{% static '/IMAGES/compression.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Compression(Head
Injury) < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal9" >


Check
< / button >
< div


class ="modal fade" id="modal9" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Compression (Head Injury) < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > An
injury
to
the
head
that
causes
compression
of
the
brain.This
can
be
due
to
swelling
of
the
brain
itself or bleeding
into
the
skull. < / p >
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
src = "{% static '/IMAGES/concussion.jpeg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Concussion(Head
Injury) < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal10" >


Check
< / button >
< div


class ="modal fade" id="modal10" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Concussion (Head Injury) < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > An
injury
to
the
brain
which
causes
'shaking' / 'jarring'
of
the
brain. < / p >
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
src = "{% static '/IMAGES/contusion.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Contusion < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal11" >


Check
< / button >
< div


class ="modal fade" id="modal11" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Contusion < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
bruise(bleeding
beneath
the
skin) < / p >
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
src = "{% static '/IMAGES/entonox.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Entonox < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal12" >


Check
< / button >
< div


class ="modal fade" id="modal12" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Entonox < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
safe
pain
killing
gas
that
can
be
given
by
ambulance
crews, sometimes
known as "gas and air". < / p >
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
src = "{% static '/IMAGES/epipen.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Epi - pen < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal13" >


Check
< / button >
< div


class ="modal fade" id="modal13" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Epi-pen < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > An
auto - injecting
syringe
containing
adrenaline
used
to
counteract
a
major
allergic
reaction. < / p >
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
src = "{% static '/IMAGES/epilepsy.jpeg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Epilepsy < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal14" >


Check
< / button >
< div


class ="modal fade" id="modal14" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Epilepsy < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
medical
condition
characterised
by
repeated
seizures.May
be
controlled
by
medication. < / p >
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
src = "{% static '/IMAGES/febrile.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Febrile
Convulsion < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal15" >


Check
< / button >
< div


class ="modal fade" id="modal15" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Febrile Convulsion < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
seizure
which
occurs in children
when
they
overheat. < / p >
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
src = "{% static '/IMAGES/fractures.jpeg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Fracture < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal16" >


Check
< / button >
< div


class ="modal fade" id="modal16" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Fracture < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > Another
term
used
for a broken bone.< / p >
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
src = "{% static '/IMAGES/heart attack.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Heart
Attack < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal17" >


Check
< / button >
< div


class ="modal fade" id="modal17" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Heart Attack < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > Blockage
of
an
artery in the
heart(coronary
artery) causing
severe
chest
pain and damage
to
heart
muscle. < / p >
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
src = "{% static '/IMAGES/hyperglycaemia.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Hyperglycaemia < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal18" >


Check
< / button >
< div


class ="modal fade" id="modal18" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Hyperglycaemia < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > High
blood
sugar
levels. < / p >
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
src = "{% static '/IMAGES/hypoglycaemia.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Hypoglycaemia < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal19" >


Check
< / button >
< div


class ="modal fade" id="modal19" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Hypoglycaemia < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > Low
blood
sugar
levels. < / p >
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
src = "{% static '/IMAGES/insulin.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Insulin < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal20" >


Check
< / button >
< div


class ="modal fade" id="modal20" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Insulin < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
hormone
produced
by
the
pancreas
that
reduces
blood
sugar
level. < / p >
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
src = "{% static '/IMAGES/laceration.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Laceration < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal21" >


Check
< / button >
< div


class ="modal fade" id="modal21" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Laceration < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > An
injury
where
there is cutting or tearing
of
the
skin. < / p >
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
src = "{% static '/IMAGES/medialert.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Medialert < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal22" >


Check
< / button >
< div


class ="modal fade" id="modal22" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Medialert < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
bracelet
which
someone
may
wear
containing
impotant
medical
information
about
them. < / p >
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
src = "{% static '/IMAGES/Meningitis.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Meningitis < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal23" >


Check
< / button >
< div


class ="modal fade" id="modal23" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Meningitis < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
life
threatning
medical
condition
where
the
protective
coverings
of
the
brain(the
meningies) become
infected and inflamed. < / p >
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
src = "{% static '/IMAGES/micropore.jpg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Micropore < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal24" >


Check
< / button >
< div


class ="modal fade" id="modal24" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Micropore < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
brand
of
medical
tape
used
to
fix
non - adhesive
dressings
over
injuries.The
tape is designed
to
be
hypoallergenic and easy
for the casuality to remove.< / p >
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
src = "{% static '/IMAGES/ministroke.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Mini
Stroke < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal25" >


Check
< / button >
< div


class ="modal fade" id="modal25" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Mini Stroke < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > Same as a
stroke, except symptoms
resolves
within
24
hours.Sometimes
called
a
"Transi Ischaemic Attack"(TIA). < / p >
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
src = "{% static '/IMAGES/openfracture.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Open
Fracture < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal26" >


Check
< / button >
< div


class ="modal fade" id="modal26" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Open Fracture < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
fracture
where
the
skin
has
been
broken
by
the
injured
bone.Sometimes
called
a
compound
fracture. < / p >
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
src = "{% static '/IMAGES/paracetamol.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Paracetamol < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal27" >


Check
< / button >
< div


class ="modal fade" id="modal27" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Paracetamol < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
common
effective
painkiller
available
over
the
counter(prescription
not needed).< / p >
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
src = "{% static '/IMAGES/primary.png' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Primary
Survey < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal28" >


Check
< / button >
< div


class ="modal fade" id="modal28" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Primary Servey < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > The
quick
initial
assesment
of
a
patient.Often
structured in an
'ABC'
approch(airway, breathing, circulation). < / p >
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
src = "/{% static 'IMAGES/recovery.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Recovery
Position < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal29" >


Check
< / button >
< div


class ="modal fade" id="modal29" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Recovery Position < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
position
where
the
casuality is laying
on
their
side
to
protect
their
airway. < / p >
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
src = "{% static '/IMAGES/salbutamol.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Salbutamol < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal30" >


Check
< / button >
< div


class ="modal fade" id="modal30" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Salbutamol < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
common
drug
used
to
treat
asthma
attacks, often
found in inhalers. < / p >
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
src = "{% static '/IMAGES/scoop.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Scoop
Stretcher < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal31" >


Check
< / button >
< div


class ="modal fade" id="modal31" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Scoop Stretcher < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > Used
to
lift
casualities
off
the
ground.Sometimes
called
an
orthopedic
stretcher. < / p >
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
src = "{% static '/IMAGES/secondary.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Secondary
Survey < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal32" >


Check
< / button >
< div


class ="modal fade" id="modal32" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Secondary Survey < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
more
detailed
assesment
of
a
patient
involving
checking
for injuries and taking observations.< / p >
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
src = "{% static '/IMAGES/seizure.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Seizure < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal33" >


Check
< / button >
< div


class ="modal fade" id="modal33" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Seizure < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > Abnormal or excessive
activity in the
brain
that
can
cause
a
variety
of
symptoms
such as muscle
movement, unconsciousness and rigidity. < / p >
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
src = "{% static '/IMAGES/Shock.jpeg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Shock < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal34" >


Check
< / button >
< div


class ="modal fade" id="modal34" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Shock < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > Inadequate
oxygen
reaching
the
tissue.Can
have
various
causes
such as blood
loss, burns or allergic
reactions. < / p >
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
src = "{% static '/IMAGES/Stroke.jpeg' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Stroke < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal35" >


Check
< / button >
< div


class ="modal fade" id="modal35" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Stroke < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
blood
clot or bleed in the
brain
causing
symptoms
such as loss
of
movement and facial
droop. < / p >
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
src = "{% static '/IMAGES/tough.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Tough
Cuts < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal36" >


Check
< / button >
< div


class ="modal fade" id="modal36" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Tough Cuts < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > Scissors
designed
for cutting clothing, seatbelts and other tough things! < / p >
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
src = "{% static '/IMAGES/tri.jfif' %}"
width = "100"
height = "70" / >
< span
style = "font-family:Georgia, 'Times New Roman', Times, serif;font-size:20px;" > & emsp; & emsp;
Triangular
Bandage < / span >
< button
type = "button"
type = "button"


class ="btn btn-secondary mx-8 my-3 float-right" data-toggle="modal" data-target="#modal37" >


Check
< / button >
< div


class ="modal fade" id="modal37" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true" >

< div


class ="modal-dialog modal-dialog-centered" role="document" >

< div


class ="modal-content" >

< div


class ="modal-header" >

< h5


class ="modal-title" id="exampleModalLongTitle" > < b > Triangular Bandage < / b > < / h5 >

< button
type = "button"


class ="close" data-dismiss="modal" aria-label="Close" >

< span
aria - hidden = "true" > & times; < / span >
< / button >
< / div >
< div


class ="modal-body" >

< p > A
triangular
shaped
piece
of
cloth
which
can
be
used
for various first aid procedures (e.g., a sling) < / p >
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
< footer


class ="container" style="margin-top: 15px" >

< p


class ="float-end" > < a href="#" > Back to top < / a > < / p >

< p >
© 2021 - 2025
MITIAN
's DOCTOR, Inc. · <a href="#">Privacy</a> ·
< a
href = "#" > Terms < / a >
< / p >
< / footer >
< !-- Optional
JavaScript -->
< !-- jQuery
first, then
Popper.js, then
Bootstrap
JS -->
< script
src = "https://code.jquery.com/jquery-3.2.1.slim.min.js"
integrity = "sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
crossorigin = "anonymous"
> < / script >
< script
src = "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
integrity = "sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
crossorigin = "anonymous"
> < / script >
< script
src = "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
integrity = "sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
crossorigin = "anonymous"
> < / script >
< / body >
< / html >