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
content = "width=device-width, initial-scale=1" / >
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
href = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
rel = "stylesheet"
integrity = "sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
crossorigin = "anonymous"
/ >
< link
rel = "stylesheet"
href = "{% static '/CSS/Drugs_by_condition.css' %}" / >
< title > Drugs
By
Condition < / title >
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


class ="nav-link active" aria-current="page" href="{% url 'home' %}" > Home < / a >

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
< form


class ="d-flex" >

< input


class ="form-control me-2"


type = "search"
placeholder = "Search"
aria - label = "Search"
/ >
< button


class ="btn btn-outline-dark mx-1" type="submit" >


Search
< / button >
< / form >
< / div >
< / div >
< / nav >
< div


class ="container" >

<

class class="container marketing" >

< !-- START
THE
FEATURETTES -->

< hr


class ="featurette-divider" >

< div


class ="row featurette" >

< div


class ="col-md-7" >

< h2


class ="featurette-heading" > Pregnancy Care < span class ="text-muted" > < / span > < / h2 >

< p


class ="lead" style="text-align: justify;" > Some medicines are safe to take during pregnancy while other medicines may have adverse effects on the unborn baby.Most medicines are assigned one of five FDA Pregnancy categories to help identify the potential level of risk.It is very important to check each and every medicine, including over-the-counter medicines and natural supplements, to determine if they are safe to take while pregnant < / p >

< a
href = "{% url 'Pregnancy_Care' %}"


class ="btn btn-outline-dark"

> Check < / a >
< / div >
< div


class ="col-md-5" >

< img


class ="featurette-image img-fluid mx-auto" data-src="holder.js/500x500/auto" alt="500x500" style="width: 400px; height: 300px; float: right;" src="{% static '/IMAGES/pregnant-woman-with-daughter.jpeg' %}" data-holder-rendered="true" >

< / div >
< / div >

< hr


class ="featurette-divider" >

< div


class ="row featurette" >

< div


class ="col-md-7 order-md-2" >

< h2


class ="featurette-heading" > Skin Infections < span class ="text-muted" > < / span > < / h2 >

< p


class ="lead"style="text-align: justify;" > Your skin is the largest organ of your body.Its function is to protect your body from infection.Sometimes the skin itself becomes infected.Skin infections are caused by a wide variety of germs, and symptoms can vary from mild to serious.Mild infections may be treatable with over-the-counter medications and home remedies, whereas other infections may require medical attention.< / p >

< a
href = "{% url 'skin_infection' %}"


class ="btn btn-outline-dark " style="float: right;"

> Check < / a > < / div >
< div


class ="col-md-5 order-md-1" >

< img


class ="featurette-image img-fluid mx-auto" data-src="holder.js/500x500/auto" alt="400x200" src="{% static '/IMAGES/skin_infections.jpeg' %}" data-holder-rendered="true" style="width: 400px; height: 300px; float: left;" >

< / div >
< / div >

< hr


class ="featurette-divider" >

< div


class ="row featurette" >

< div


class ="col-md-7" >

< h2


class ="featurette-heading" > Wounds and Burns < span class ="text-muted" > < / span > < / h2 >

< p


class ="lead" style="text-align: justify;" > Wounds are injuries that break the skin or other body tissues.They include cuts, scrapes, scratches, and punctured skin.They often happen because of an accident, but surgery, sutures, and stitches also cause wounds Burns are one of the most common household injuries, especially among children.The term “burn” means more than the burning sensation associated with this injury.Burns are characterized by severe skin damage that causes the affected skin cells to die.

< / p > < a
href = "{% url 'wounds'%}"


class ="btn btn-outline-dark"

> Check < / a > < / div >
< div


class ="col-md-5" >

< img


class ="featurette-image img-fluid mx-auto" data-src="holder.js/500x500/auto" alt="500x500" src="{% static '/IMAGES/wound.jpeg' %}" data-holder-rendered="true" style="width: 400px; height: 300px; float: right;" >

< / div >
< / div >
< hr


class ="featurette-divider" >

< hr


class ="featurette-divider" >

< hr


class ="featurette-divider" >

< !-- / END
THE
FEATURETTES -->

< / div >
< / div >
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
JavaScript;
choose
one
of
the
two! -->

< !-- Option
1: Bootstrap
Bundle
with Popper -->
< script
src = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"
integrity = "sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW"
crossorigin = "anonymous"
> < / script >

< !-- Option
2: Separate
Popper and Bootstrap
JS -->
< !--
< script
src = "https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"
integrity = "sha384-q2kxQ16AaE6UbzuKqyBE9/u/KzioAlnx2maXQHiDX9d4/zp8Ok3f+M7DPm+Ib6IU"
crossorigin = "anonymous" > < / script >
< script
src = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.min.js"
integrity = "sha384-pQQkAEnwaBkjpqZ8RU1fF1AKtTcHJwFl3pblpTlHXybJjHpMYo79HY3hIi4NKxyj"
crossorigin = "anonymous" > < / script >
-->
< / body >
< / html >