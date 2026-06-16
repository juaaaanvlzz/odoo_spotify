from odoo import api, models, fields


class SpotifyArtist(models.Model):
    _name = "spotify.artist"
    _description = "Artist"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    image = fields.Binary(string="Photo", attachment=True)
    biography = fields.Text(string="Biography")
    genre = fields.Selection(
        [
            ("pop", "Pop"),
            ("rock", "Rock"),
            ("hiphop", "Hip-Hop"),
            ("electronic", "Electronic"),
            ("jazz", "Jazz"),
            ("classical", "Classical"),
            ("reggaeton", "Reggaeton"),
            ("latin", "Latin"),
            ("rnb", "R&B"),
            ("indie", "Indie"),
            ("metal", "Metal"),
            ("folk", "Folk"),
            ("podcast", "Podcast"),
            ("other", "Other"),
        ],
        string="Genre",
        required=True,
    )
    album_ids = fields.One2many(
        "spotify.album", "artist_id", string="Albums"
    )
    track_count = fields.Integer(
        string="Track Count",
        compute="_compute_track_count",
        store=True,
    )

    @api.depends("album_ids.track_ids")
    def _compute_track_count(self):
        for artist in self:
            artist.track_count = sum(
                len(album.track_ids) for album in artist.album_ids
            )
