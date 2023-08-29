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
content = "width=device-width, initial-scale=1" >
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
href = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
rel = "stylesheet"
integrity = "sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
crossorigin = "anonymous" >
< link
rel = "stylesheet"
href = "{% static '/CSS/Bacterial_Inf.css' %}" >
< title > Bacterial
Infection
Med < / title >
< / head >
< body >
< nav


class ="navbar navbar-expand-lg navbar-light" >

< div


class ="container-fluid" >

< a


class ="navbar-brand" href="#" > MITIAN's DOCTOR</a>

< button


class ="navbar-toggler" type="button" data-bs-toggle="collapse"


data - bs - target = "#navbarSupportedContent"
aria - controls = "navbarSupportedContent"
aria - expanded = "false"
aria - label = "Toggle navigation" >
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


class ="nav-link" href="{% url 'Bacterial' %}" > About < / a >

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
< ul
style = "list-style-type: none" >
{ %
for medicine in list %}
< form
method = "GET"
action = "{% url 'Soft_Tissue' %}" >
{ % csrf_token %}
< li > < button
name = "term"


class ="buton btn btn-outline-dark" style="width:100%; margin-top:4px;border: palegreen ;text-align: left;" value="{{medicine}}" onclick="dothis(this.value)" > {{medicine}} < / button > < / li >

< / form >
{ % endfor %}
< / ul >

< footer


class ="container" style="margin-top: 15px ;" >

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
src = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
integrity = "sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
crossorigin = "anonymous" > < / script >

< !-- Option
2: Separate
Popper and Bootstrap
JS -->
< !--
< script
src = "https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js"
integrity = "sha384-SR1sx49pcuLnqZUnnPwx6FCym0wLsk5JZuNx2bPPENzswTNFaQU1RDvt3wT4gWFG"
crossorigin = "anonymous" > < / script >
< script
src = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.min.js"
integrity = "sha384-j0CNLUeiqtyaRmlzUHCPZ+Gy5fQu0dQ6eZ/xAww941Ai1SxSY+0EQqNXNE6DZiVc"
crossorigin = "anonymous" > < / script >
-->
< / body >
< / html >
