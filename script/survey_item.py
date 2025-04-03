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

    id: str = None
    related_id: str = None
    class_: str = field(default=None, metadata={"alias": "class"})
    type_and_scale: str = field(default=None, metadata={"alias": "type/scale"})
    name: str = None
    relevance: str = None
    text: str = None
    help: str = None
    language: str = None
    validation: str = None
    mandatory: str = None
    encrypted: str = None
    other: str = None
    default: str = None
    same_default: str = None
    same_script: str = None
    allowed_filetypes: str = None
    alphasort: str = None
    answer_order: str = None
    answer_width: str = None
    answer_width_bycolumn: str = None
    array_filter: str = None
    array_filter_exclude: str = None
    array_filter_style: str = None
    assessment_value: str = None
    category_separator: str = None
    choice_input_columns: str = None
    choice_title: str = None
    commented_checkbox: str = None
    commented_checkbox_auto: str = None
    cssclass: str = None
    date_format: str = None
    date_max: str = None
    date_min: str = None
    display_columns: str = None
    display_rows: str = None
    display_type: str = None
    dropdown_dates: str = None
    dropdown_dates_minute_step: str = None
    dropdown_dates_month_style: str = None
    dropdown_prefix: str = None
    dropdown_prepostfix: str = None
    dropdown_separators: str = None
    dropdown_size: str = None
    dualscale_headerA: str = None
    dualscale_headerB: str = None
    em_validation_q: str = None
    em_validation_q_tip: str = None
    em_validation_sq: str = None
    em_validation_sq_tip: str = None
    equals_num_value: str = None
    equation: str = None
    exclude_all_others: str = None
    exclude_all_others_auto: str = None
    hidden: str = None
    hide_tip: str = None
    input_boxes: str = None
    input_size: str = None
    label_input_columns: str = None
    location_city: str = None
    location_country: str = None
    location_defaultcoordinates: str = None
    location_mapheight: str = None
    location_mapservice: str = None
    location_mapwidth: str = None
    location_mapzoom: str = None
    location_nodefaultfromip: str = None
    location_postal: str = None
    location_state: str = None
    max_answers: str = None
    max_filesize: str = None
    max_num_of_files: str = None
    max_num_value: str = None
    max_num_value_n: str = None
    max_subquestions: str = None
    maximum_chars: str = None
    min_answers: str = None
    min_num_of_files: str = None
    min_num_value: str = None
    min_num_value_n: str = None
    multiflexible_checkbox: str = None
    multiflexible_max: str = None
    multiflexible_min: str = None
    multiflexible_step: str = None
    num_value_int_only: str = None
    numbers_only: str = None
    other_comment_mandatory: str = None
    other_numbers_only: str = None
    other_replace_text: str = None
    page_break: str = None
    parent_order: str = None
    placeholder: str = None
    prefix: str = None
    printable_help: str = None
    public_statistics: str = None
    random_group: str = None
    random_order: str = None
    rank_title: str = None
    repeat_headings: str = None
    reverse: str = None
    samechoiceheight: str = None
    samelistheight: str = None
    scale_export: str = None
    show_comment: str = None
    show_grand_total: str = None
    show_title: str = None
    show_totals: str = None
    showpopups: str = None
    slider_accuracy: str = None
    slider_custom_handle: str = None
    slider_default: str = None
    slider_default_set: str = None
    slider_handle: str = None
    slider_layout: str = None
    slider_max: str = None
    slider_middlestart: str = None
    slider_min: str = None
    slider_orientation: str = None
    slider_rating: str = None
    slider_reset: str = None
    slider_reversed: str = None
    slider_separator: str = None
    slider_showminmax: str = None
    statistics_graphtype: str = None
    statistics_showgraph: str = None
    statistics_showmap: str = None
    suffix: str = None
    text_input_columns: str = None
    text_input_width: str = None
    time_limit: str = None
    time_limit_action: str = None
    time_limit_countdown_message: str = None
    time_limit_disable_next: str = None
    time_limit_disable_prev: str = None
    time_limit_message: str = None
    time_limit_message_delay: str = None
    time_limit_message_style: str = None
    time_limit_timer_style: str = None
    time_limit_warning: str = None
    time_limit_warning_2: str = None
    time_limit_warning_2_display_time: str = None
    time_limit_warning_2_message: str = None
    time_limit_warning_2_style: str = None
    time_limit_warning_display_time: str = None
    time_limit_warning_message: str = None
    time_limit_warning_style: str = None
    use_dropdown: str = None
    value_range_allows_missing: str = None



# sottocategorie di "survey_item" possibili

class group(survey_item):
    def __init__(self, type_and_scale: str, name: str):
        super().__init__()
        
        self.class_ = "G"
        self.type_and_scale = type_and_scale
        self.name = name
        self.language = "it"

class question(survey_item):
    def __init__(self,  name: str, text: str,  type_and_scale: str = "L", mandatory: str = "Y"):
        super().__init__()

        self.class_ = "Q"
        self.type_and_scale = type_and_scale
        self.name = name
        self.relevance = "1"
        self.text = text
        self.language = "it"
        self.mandatory = mandatory


class sub_question(survey_item):
    def __init__(self, type_and_scale: str, name: str, text: str, mandatory: str):
        super().__init__()

        self.class_ = "SQ"
        self.type_and_scale = type_and_scale
        self.name = name
        self.relevance = "1"
        self.text = text
        self.language = "it"
        self.mandatory = mandatory

class answer(survey_item):
    def __init__(self,  name: str, text: str):
        super().__init__()
        
        self.class_ = "A"
        self.type_and_scale = "0"
        self.name = name
        self.text = text
        self.language = "it"