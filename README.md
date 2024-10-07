# Flamingo Terrace

Para comenzar con la presentacion de este projecto me tomare la libertad de contarles un poco de mi vida primero.
Soy cocinero, esa ha sido mi profecion al menos los ultimos 10 años de mi vida. Algo bastante alejado de la programacion pero que tiene algo en comun con ella, ambas son grandes herramientas para construir cosas.
Ya no me da el cuerpo para seguir trabajando en una cocina, por lo que tuve que buscar otro rumbo. Nunaca llegué a tener mi propio restarurant, talvez en un futuro exista fisicamente, pero por el momento lo pueden visitar en la web.

El desarrollo de este projecto se podria decir que nacio hace 5 meses en el primer projecto ( link: https://fenasti.github.io/Catering/index.html ). Luego de desarrollar la pagina web para unos clientes con un projecto de catering llamado Flamingo, podemos ver que el negocio ha prosperado y han podido mudarse a su propio local permanente.
Logicamente este nuevo negocio necesita un rebranding y refrescar su concepto para esta nueva etapa.

### La propuesta fue la siguente:

Se conservaria el logo y la escencia lúdica de su presentacion enfocada en un rosa inspirado en el color del Flamenco.
La paleta de colores se eligiria a partir del mismo color de dicho logo (#E94578), un rosa brillante que evoca los colores chillantes del verano.
Buscando una paleta minimalista se le pidió a un generador de colores complemetarios que diera uno que jugase con el rosa, el negro y el blanco. El color que generó (#33202A) fue un morado perfecto para darle un tpque de sobriedad al rosa tan fuerte que propone lo contrario.

## Problems / Bugs

The first problem i had after trying the early deploymnet was that i was using the wrong name project in the Procfile. I was using a previous project name as a copy-paste way without realizing the importance of the path

After installing Postgress and migrate the changes of the first model formulated, i faced another bug wich took me a lot of time to solve, until i added the 8000 port to the CSRF_TRUSTED_ORIGINS besides the ALLOWED_HOSTS.

After creating the superuser and migrate the first modelof Django, I deployed the project to Heroku and an "Internat Server Error" was shown. I solved it providing a SECRET_KEY variable to the Vars settings in Heroku.

I couldn't visualize the view of my Home model, this was because the template provided in the class view of the index app was not written as a relative path.

Mentor told me the input specified was not valid 

After a whole day trying to implement the callendar input i decided to come back to the main stage using the command "git log" to view my later logs and as i didn't commit during the whole time because there were no succesfull stages, i used the command "git checkout --." and came back to the previous stage.
First i tried to use an extension called Tempus Dominus nut it was too complicated to install thru all the JavaScript and all the metadata needed. The main problem was that afer to be able to show a callendar input, the data was given all date and time together and somehow the default format couldn't accept it in any way i tried. Changing the default format to many different acceptance criterias.
After returning to the previous stage i decided to separate the specifications input to both time and date respectively and combine them afterwards to use them as the database reservation_datetime object required.

## Development Process

The project started with the ideation process, in paper i wrote what SHOULD be in the project:

- A base.html template with a nav-bar and a footer
- A Home/Index template as the homepage.
- Reservations app and template with a form to request a reservation.
- An about.html where is some information of the restaurant.
- Access to a web version of the menu.

I decided to separate it in 3 main href link paths and to provide he menu as a donwload pdf link also in the nav-bar.
As the Signup, Signin and Logout pages and all the client user functions would be exclusive related to the Reservation view, i solved to blend and display all together in the same place with conditional URL paths.

### Agile process

First is to create the repository of the project using the code-institute template provided. Creation of the Project instance and connect it to the project repository. Using Agile to separate themain function in the most basic task to build the apps with the issues User Story template that was was previous created and display it in the Issues board separating them in All, In Progress, Done and Not Implemented for the functions that were not possible to add to the project because of lack of time or current experience.



