import numpy as np

def create_cambridge_probe(probe_type='cambridge M2'):
    """
    Create `ProbeType` and `Electrode` for cambridge probes:
    1.0 (M2)
    For electrode location, the (0, 0) is the
    bottom left corner of the probe (ignore the tip portion)
    Electrode numbering is 1-indexing
    """

    def build_electrodes(site_count, col_spacing, row_spacing,
                        white_spacing, col_count=1,
                        shank_count=1, shank_spacing=31):
        """
        :param site_count: site count per shank
        :param col_spacing: (um) horrizontal spacing between sites
        :param row_spacing: (um) vertical spacing between columns
        :param white_spacing: (um) offset spacing
        :param col_count: number of column per shank
        :param shank_count: number of shank
        :param shank_spacing: spacing between shanks
        :return:
        """
        row_count = int(site_count / col_count)
        x_coords = np.tile([0, 0 + col_spacing], row_count)
        x_white_spaces = np.tile([white_spacing, white_spacing, 0, 0], int(row_count / col_count))

        x_coords = x_coords + x_white_spaces
        y_coords = np.repeat(np.arange(row_count) * row_spacing, col_count)
        shank_cols = np.tile([0, 1], row_count)
        shank_rows = np.repeat(range(row_count), col_count)

        npx_electrodes = []
        for shank_no in range(shank_count):
            npx_electrodes.extend([{'electrode': (site_count * shank_no) + e_id,
                                    'shank': shank_no,
                                    'shank_col': c_id,
                                    'shank_row': r_id,
                                    'x_coord': x + (shank_no * shank_spacing),
                                    'y_coord': y}
                                for e_id, (c_id, r_id, x, y) in enumerate(
                zip(shank_cols, shank_rows, x_coords, y_coords))])

        return npx_electrodes

    # ---- 1.0 3A ----
    if probe_type == 'cambridge M2':
        electrodes = build_electrodes(site_count=64, col_spacing=0, row_spacing=31,
                                    white_spacing=0, col_count=1)

    return electrodes

electrodes = create_cambridge_probe(probe_type='cambridge M2')