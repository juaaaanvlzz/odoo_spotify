from odoo import api, models, fields


class SpotifyTrack(models.Model):
    _name = "spotify.track"
    _description = "Track"
    _order = "album_id, sequence, name"

    name = fields.Char(string="Title", required=True)
    sequence = fields.Integer(string="Track Number", default=1)
    duration = fields.Integer(
        string="Duration (seconds)", required=True, default=0
    )
    duration_formatted = fields.Char(
        string="Duration",
        compute="_compute_duration_formatted",
    )
    audio_file = fields.Binary(string="Audio File", attachment=True)
    stream_url = fields.Char(string="Stream URL")
    play_count = fields.Integer(
        string="Play Count", default=0, readonly=True
    )
    album_id = fields.Many2one(
        "spotify.album", string="Album", required=True, ondelete="cascade"
    )
    artist_id = fields.Many2one(
        string="Artist",
        related="album_id.artist_id",
        store=True,
        readonly=True,
    )
    artist_name = fields.Char(
        string="Artist Name",
        related="album_id.artist_name",
        store=True,
    )
    album_name = fields.Char(
        string="Album Title", related="album_id.name", store=True
    )

    @api.depends("duration")
    def _compute_duration_formatted(self):
        for track in self:
            if track.duration:
                minutes = track.duration // 60
                seconds = track.duration % 60
                track.duration_formatted = f"{minutes}:{seconds:02d}"
            else:
                track.duration_formatted = "0:00"

    def action_play_track(self):
        self.ensure_one()
        self.sudo().play_count += 1
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": "Now Playing",
                "message": f"{self.name} - {self.artist_name}",
                "type": "success",
                "sticky": False,
                "next": {"type": "ir.actions.act_window_close"},
            },
        }
