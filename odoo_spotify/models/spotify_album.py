from odoo import api, models, fields


class SpotifyAlbum(models.Model):
    _name = "spotify.album"
    _description = "Album"
    _order = "release_date desc, name"

    name = fields.Char(string="Title", required=True)
    cover = fields.Binary(string="Cover Art", attachment=True)
    release_date = fields.Date(string="Release Date")
    album_type = fields.Selection(
        [
            ("album", "Album"),
            ("single", "Single"),
            ("ep", "EP"),
            ("compilation", "Compilation"),
        ],
        string="Type",
        default="album",
        required=True,
    )
    artist_id = fields.Many2one(
        "spotify.artist", string="Artist", required=True, ondelete="cascade"
    )
    artist_name = fields.Char(
        string="Artist Name", related="artist_id.name", store=True
    )
    track_ids = fields.One2many(
        "spotify.track", "album_id", string="Tracks"
    )
    track_count = fields.Integer(
        string="Track Count", compute="_compute_track_count", store=True
    )
    total_duration = fields.Integer(
        string="Total Duration (s)",
        compute="_compute_total_duration",
        store=True,
    )

    @api.depends("track_ids")
    def _compute_track_count(self):
        for album in self:
            album.track_count = len(album.track_ids)

    @api.depends("track_ids.duration")
    def _compute_total_duration(self):
        for album in self:
            album.total_duration = sum(
                album.track_ids.mapped("duration")
            )
