from dataclasses import dataclass, field
from typing import Any

# "survey_item" rappresenta la singola riga dell'output:
# contiene come variabili ogni colonna possibile dell'intestazione del questionario.
# l'unione di più "survey_item" rapprensenta il questionario

# è necessario introdurre @dataclass per evitare errori in fase di serializzazione 
# in quanto due delle variabili utilizzate vanno in conflitto con le keyword riservate di Python,  
# in particolare le seguenti variabili sono state riscritte con gli alias:

# class -> class_
# type/scale -> type_and_scale

@dataclass
class survey_item:

    # class -> class_
    # type/scale -> type_and_scale

    id = None
    related_id = None
    class_ = field(default=None, metadata={"alias": "class"})
    type_and_scale = field(default=None, metadata={"alias": "type/scale"})
    name = None
    relevance = None
    text = None
    help = None
    language = None
    validation = None
    mandatory = None
    encrypted = None
    other = None
    default = None
    same_default = None
    same_script = None
    allowed_filetypes = None
    alphasort = None
    answer_order = None
    answer_width = None
    answer_width_bycolumn = None
    array_filter = None
    array_filter_exclude = None
    array_filter_style = None
    assessment_value = None
    category_separator = None
    choice_input_columns = None
    choice_title = None
    commented_checkbox = None
    commented_checkbox_auto = None
    cssclass = None
    date_format = None
    date_max = None
    date_min = None
    display_columns = None
    display_rows = None
    display_type = None
    dropdown_dates = None
    dropdown_dates_minute_step = None
    dropdown_dates_month_style = None
    dropdown_prefix = None
    dropdown_prepostfix = None
    dropdown_separators = None
    dropdown_size = None
    dualscale_headerA = None
    dualscale_headerB = None
    em_validation_q = None
    em_validation_q_tip = None
    em_validation_sq = None
    em_validation_sq_tip = None
    equals_num_value = None
    equation = None
    exclude_all_others = None
    exclude_all_others_auto = None
    hidden = None
    hide_tip = None
    input_boxes = None
    input_size = None
    label_input_columns = None
    location_city = None
    location_country = None
    location_defaultcoordinates = None
    location_mapheight = None
    location_mapservice = None
    location_mapwidth = None
    location_mapzoom = None
    location_nodefaultfromip = None
    location_postal = None
    location_state = None
    max_answers = None
    max_filesize = None
    max_num_of_files = None
    max_num_value = None
    max_num_value_n = None
    max_subquestions = None
    maximum_chars = None
    min_answers = None
    min_num_of_files = None
    min_num_value = None
    min_num_value_n = None
    multiflexible_checkbox = None
    multiflexible_max = None
    multiflexible_min = None
    multiflexible_step = None
    num_value_int_only = None
    numbers_only = None
    other_comment_mandatory = None
    other_numbers_only = None
    other_replace_text = None
    page_break = None
    parent_order = None
    placeholder = None
    prefix = None
    printable_help = None
    public_statistics = None
    random_group = None
    random_order = None
    rank_title = None
    repeat_headings = None
    reverse = None
    samechoiceheight = None
    samelistheight = None
    scale_export = None
    show_comment = None
    show_grand_total = None
    show_title = None
    show_totals = None
    showpopups = None
    slider_accuracy = None
    slider_custom_handle = None
    slider_default = None
    slider_default_set = None
    slider_handle = None
    slider_layout = None
    slider_max = None
    slider_middlestart = None
    slider_min = None
    slider_orientation = None
    slider_rating = None
    slider_reset = None
    slider_reversed = None
    slider_separator = None
    slider_showminmax = None
    statistics_graphtype = None
    statistics_showgraph = None
    statistics_showmap = None
    suffix = None
    text_input_columns = None
    text_input_width = None
    time_limit = None
    time_limit_action = None
    time_limit_countdown_message = None
    time_limit_disable_next = None
    time_limit_disable_prev = None
    time_limit_message = None
    time_limit_message_delay = None
    time_limit_message_style = None
    time_limit_timer_style = None
    time_limit_warning = None
    time_limit_warning_2 = None
    time_limit_warning_2_display_time = None
    time_limit_warning_2_message = None
    time_limit_warning_2_style = None
    time_limit_warning_display_time = None
    time_limit_warning_message = None
    time_limit_warning_style = None
    use_dropdown = None
    value_range_allows_missing = None
