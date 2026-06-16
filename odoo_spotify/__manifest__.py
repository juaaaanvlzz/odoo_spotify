{
    "name": "Odoo Spotify",
    "version": "17.0.1.0.0",
    "category": "Entertainment",
    "summary": "Plataforma de entretenimiento musical y podcasting",
    "description": """
Módulo de entretenimiento inspirado en Spotify para Odoo.
Permite gestionar artistas, álbumes, canciones y listas de reproducción
con una interfaz visual moderna tipo reproductor multimedia.
    """,
    "author": "Odoo Spotify Dev",
    "website": "https://github.com/odoo-spotify",
    "license": "LGPL-3",
    "depends": ["base", "web"],
    "data": [
        "security/spotify_groups.xml",
        "security/ir.model.access.csv",
        "views/spotify_artist_views.xml",
        "views/spotify_album_views.xml",
        "views/spotify_track_views.xml",
        "views/spotify_playlist_views.xml",
        "views/spotify_menu.xml",
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "icon": "/odoo_spotify/static/description/icon.png",
}
