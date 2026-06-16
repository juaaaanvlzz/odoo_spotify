from odoo import api, models, fields


class SpotifyPlaylist(models.Model):
    _name = "spotify.playlist"
    _description = "Playlist"
    _order = "create_date desc"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    user_id = fields.Many2one(
        "res.users",
        string="Created by",
        default=lambda self: self.env.user,
        required=True,
    )
    track_ids = fields.Many2many(
        "spotify.track",
        "spotify_playlist_track_rel",
        "playlist_id",
        "track_id",
        string="Tracks",
    )
    is_public = fields.Boolean(
        string="Public Playlist", default=False
    )
    track_count = fields.Integer(
        string="Track Count",
        compute="_compute_track_count",
        store=True,
    )
    total_duration = fields.Integer(
        string="Total Duration (s)",
        compute="_compute_total_duration",
        store=True,
    )

    @api.depends("track_ids")
    def _compute_track_count(self):
        for playlist in self:
            playlist.track_count = len(playlist.track_ids)

    @api.depends("track_ids.duration")
    def _compute_total_duration(self):
        for playlist in self:
            playlist.total_duration = sum(
                playlist.track_ids.mapped("duration")
            )
