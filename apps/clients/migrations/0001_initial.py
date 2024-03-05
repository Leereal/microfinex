# Generated by Django 5.0.2 on 2024-03-05 05:47

import django.contrib.postgres.fields
import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("branches", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=30, region=None, verbose_name="phone number"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Cellphone", "Cellphone"),
                            ("Home", "Home"),
                            ("Work", "Work"),
                            ("Other", "Other"),
                        ],
                        default="Other",
                        max_length=20,
                        verbose_name="Contact Type",
                    ),
                ),
                (
                    "is_primary",
                    models.BooleanField(default=False, verbose_name="Primary"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                (
                    "whatsapp",
                    models.BooleanField(default=False, verbose_name="WhatsApp"),
                ),
            ],
            options={
                "verbose_name": "Client Contact",
                "verbose_name_plural": "Client Contacts",
            },
        ),
        migrations.CreateModel(
            name="NextOfKin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_modified", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Last Name"),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        null=True,
                        region=None,
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "relationship",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Relationship",
                    ),
                ),
                (
                    "address",
                    models.TextField(blank=True, null=True, verbose_name="Address"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
            ],
            options={
                "verbose_name": "Next of Kin",
                "verbose_name_plural": "Next of Kin",
            },
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_modified", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Last Name"),
                ),
                (
                    "emails",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.EmailField(
                            max_length=254, verbose_name="Email"
                        ),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                        verbose_name="Emails",
                    ),
                ),
                (
                    "national_id",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        unique=True,
                        verbose_name="National ID",
                    ),
                ),
                (
                    "nationality",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Nationality",
                    ),
                ),
                (
                    "passport_number",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        unique=True,
                        verbose_name="Passport Number",
                    ),
                ),
                (
                    "passport_country",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AF", "Afghanistan"),
                            ("AX", "Åland Islands"),
                            ("AL", "Albania"),
                            ("DZ", "Algeria"),
                            ("AS", "American Samoa"),
                            ("AD", "Andorra"),
                            ("AO", "Angola"),
                            ("AI", "Anguilla"),
                            ("AQ", "Antarctica"),
                            ("AG", "Antigua and Barbuda"),
                            ("AR", "Argentina"),
                            ("AM", "Armenia"),
                            ("AW", "Aruba"),
                            ("AU", "Australia"),
                            ("AT", "Austria"),
                            ("AZ", "Azerbaijan"),
                            ("BS", "Bahamas"),
                            ("BH", "Bahrain"),
                            ("BD", "Bangladesh"),
                            ("BB", "Barbados"),
                            ("BY", "Belarus"),
                            ("BE", "Belgium"),
                            ("BZ", "Belize"),
                            ("BJ", "Benin"),
                            ("BM", "Bermuda"),
                            ("BT", "Bhutan"),
                            ("BO", "Bolivia"),
                            ("BQ", "Bonaire, Sint Eustatius and Saba"),
                            ("BA", "Bosnia and Herzegovina"),
                            ("BW", "Botswana"),
                            ("BV", "Bouvet Island"),
                            ("BR", "Brazil"),
                            ("IO", "British Indian Ocean Territory"),
                            ("BN", "Brunei"),
                            ("BG", "Bulgaria"),
                            ("BF", "Burkina Faso"),
                            ("BI", "Burundi"),
                            ("CV", "Cabo Verde"),
                            ("KH", "Cambodia"),
                            ("CM", "Cameroon"),
                            ("CA", "Canada"),
                            ("KY", "Cayman Islands"),
                            ("CF", "Central African Republic"),
                            ("TD", "Chad"),
                            ("CL", "Chile"),
                            ("CN", "China"),
                            ("CX", "Christmas Island"),
                            ("CC", "Cocos (Keeling) Islands"),
                            ("CO", "Colombia"),
                            ("KM", "Comoros"),
                            ("CG", "Congo"),
                            ("CD", "Congo (the Democratic Republic of the)"),
                            ("CK", "Cook Islands"),
                            ("CR", "Costa Rica"),
                            ("CI", "Côte d'Ivoire"),
                            ("HR", "Croatia"),
                            ("CU", "Cuba"),
                            ("CW", "Curaçao"),
                            ("CY", "Cyprus"),
                            ("CZ", "Czechia"),
                            ("DK", "Denmark"),
                            ("DJ", "Djibouti"),
                            ("DM", "Dominica"),
                            ("DO", "Dominican Republic"),
                            ("EC", "Ecuador"),
                            ("EG", "Egypt"),
                            ("SV", "El Salvador"),
                            ("GQ", "Equatorial Guinea"),
                            ("ER", "Eritrea"),
                            ("EE", "Estonia"),
                            ("SZ", "Eswatini"),
                            ("ET", "Ethiopia"),
                            ("FK", "Falkland Islands (Malvinas)"),
                            ("FO", "Faroe Islands"),
                            ("FJ", "Fiji"),
                            ("FI", "Finland"),
                            ("FR", "France"),
                            ("GF", "French Guiana"),
                            ("PF", "French Polynesia"),
                            ("TF", "French Southern Territories"),
                            ("GA", "Gabon"),
                            ("GM", "Gambia"),
                            ("GE", "Georgia"),
                            ("DE", "Germany"),
                            ("GH", "Ghana"),
                            ("GI", "Gibraltar"),
                            ("GR", "Greece"),
                            ("GL", "Greenland"),
                            ("GD", "Grenada"),
                            ("GP", "Guadeloupe"),
                            ("GU", "Guam"),
                            ("GT", "Guatemala"),
                            ("GG", "Guernsey"),
                            ("GN", "Guinea"),
                            ("GW", "Guinea-Bissau"),
                            ("GY", "Guyana"),
                            ("HT", "Haiti"),
                            ("HM", "Heard Island and McDonald Islands"),
                            ("VA", "Holy See"),
                            ("HN", "Honduras"),
                            ("HK", "Hong Kong"),
                            ("HU", "Hungary"),
                            ("IS", "Iceland"),
                            ("IN", "India"),
                            ("ID", "Indonesia"),
                            ("IR", "Iran"),
                            ("IQ", "Iraq"),
                            ("IE", "Ireland"),
                            ("IM", "Isle of Man"),
                            ("IL", "Israel"),
                            ("IT", "Italy"),
                            ("JM", "Jamaica"),
                            ("JP", "Japan"),
                            ("JE", "Jersey"),
                            ("JO", "Jordan"),
                            ("KZ", "Kazakhstan"),
                            ("KE", "Kenya"),
                            ("KI", "Kiribati"),
                            ("KW", "Kuwait"),
                            ("KG", "Kyrgyzstan"),
                            ("LA", "Laos"),
                            ("LV", "Latvia"),
                            ("LB", "Lebanon"),
                            ("LS", "Lesotho"),
                            ("LR", "Liberia"),
                            ("LY", "Libya"),
                            ("LI", "Liechtenstein"),
                            ("LT", "Lithuania"),
                            ("LU", "Luxembourg"),
                            ("MO", "Macao"),
                            ("MG", "Madagascar"),
                            ("MW", "Malawi"),
                            ("MY", "Malaysia"),
                            ("MV", "Maldives"),
                            ("ML", "Mali"),
                            ("MT", "Malta"),
                            ("MH", "Marshall Islands"),
                            ("MQ", "Martinique"),
                            ("MR", "Mauritania"),
                            ("MU", "Mauritius"),
                            ("YT", "Mayotte"),
                            ("MX", "Mexico"),
                            ("FM", "Micronesia (Federated States of)"),
                            ("MD", "Moldova"),
                            ("MC", "Monaco"),
                            ("MN", "Mongolia"),
                            ("ME", "Montenegro"),
                            ("MS", "Montserrat"),
                            ("MA", "Morocco"),
                            ("MZ", "Mozambique"),
                            ("MM", "Myanmar"),
                            ("NA", "Namibia"),
                            ("NR", "Nauru"),
                            ("NP", "Nepal"),
                            ("NL", "Netherlands"),
                            ("NC", "New Caledonia"),
                            ("NZ", "New Zealand"),
                            ("NI", "Nicaragua"),
                            ("NE", "Niger"),
                            ("NG", "Nigeria"),
                            ("NU", "Niue"),
                            ("NF", "Norfolk Island"),
                            ("KP", "North Korea"),
                            ("MK", "North Macedonia"),
                            ("MP", "Northern Mariana Islands"),
                            ("NO", "Norway"),
                            ("OM", "Oman"),
                            ("PK", "Pakistan"),
                            ("PW", "Palau"),
                            ("PS", "Palestine, State of"),
                            ("PA", "Panama"),
                            ("PG", "Papua New Guinea"),
                            ("PY", "Paraguay"),
                            ("PE", "Peru"),
                            ("PH", "Philippines"),
                            ("PN", "Pitcairn"),
                            ("PL", "Poland"),
                            ("PT", "Portugal"),
                            ("PR", "Puerto Rico"),
                            ("QA", "Qatar"),
                            ("RE", "Réunion"),
                            ("RO", "Romania"),
                            ("RU", "Russia"),
                            ("RW", "Rwanda"),
                            ("BL", "Saint Barthélemy"),
                            ("SH", "Saint Helena, Ascension and Tristan da Cunha"),
                            ("KN", "Saint Kitts and Nevis"),
                            ("LC", "Saint Lucia"),
                            ("MF", "Saint Martin (French part)"),
                            ("PM", "Saint Pierre and Miquelon"),
                            ("VC", "Saint Vincent and the Grenadines"),
                            ("WS", "Samoa"),
                            ("SM", "San Marino"),
                            ("ST", "Sao Tome and Principe"),
                            ("SA", "Saudi Arabia"),
                            ("SN", "Senegal"),
                            ("RS", "Serbia"),
                            ("SC", "Seychelles"),
                            ("SL", "Sierra Leone"),
                            ("SG", "Singapore"),
                            ("SX", "Sint Maarten (Dutch part)"),
                            ("SK", "Slovakia"),
                            ("SI", "Slovenia"),
                            ("SB", "Solomon Islands"),
                            ("SO", "Somalia"),
                            ("ZA", "South Africa"),
                            ("GS", "South Georgia and the South Sandwich Islands"),
                            ("KR", "South Korea"),
                            ("SS", "South Sudan"),
                            ("ES", "Spain"),
                            ("LK", "Sri Lanka"),
                            ("SD", "Sudan"),
                            ("SR", "Suriname"),
                            ("SJ", "Svalbard and Jan Mayen"),
                            ("SE", "Sweden"),
                            ("CH", "Switzerland"),
                            ("SY", "Syria"),
                            ("TW", "Taiwan"),
                            ("TJ", "Tajikistan"),
                            ("TZ", "Tanzania"),
                            ("TH", "Thailand"),
                            ("TL", "Timor-Leste"),
                            ("TG", "Togo"),
                            ("TK", "Tokelau"),
                            ("TO", "Tonga"),
                            ("TT", "Trinidad and Tobago"),
                            ("TN", "Tunisia"),
                            ("TR", "Türkiye"),
                            ("TM", "Turkmenistan"),
                            ("TC", "Turks and Caicos Islands"),
                            ("TV", "Tuvalu"),
                            ("UG", "Uganda"),
                            ("UA", "Ukraine"),
                            ("AE", "United Arab Emirates"),
                            ("GB", "United Kingdom"),
                            ("UM", "United States Minor Outlying Islands"),
                            ("US", "United States of America"),
                            ("UY", "Uruguay"),
                            ("UZ", "Uzbekistan"),
                            ("VU", "Vanuatu"),
                            ("VE", "Venezuela"),
                            ("VN", "Vietnam"),
                            ("VG", "Virgin Islands (British)"),
                            ("VI", "Virgin Islands (U.S.)"),
                            ("WF", "Wallis and Futuna"),
                            ("EH", "Western Sahara"),
                            ("YE", "Yemen"),
                            ("ZM", "Zambia"),
                            ("ZW", "Zimbabwe"),
                            ("", "Select Country"),
                        ],
                        max_length=200,
                        null=True,
                        verbose_name="passport country",
                    ),
                ),
                (
                    "photo",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Photo"
                    ),
                ),
                ("date_of_birth", models.DateField(verbose_name="Date of Birth")),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Dr", "Dr"),
                            ("Miss", "Miss"),
                            ("Mr", "Mr"),
                            ("Mrs", "Mrs"),
                            ("Ms", "Ms"),
                            ("Prof", "Prof"),
                        ],
                        max_length=10,
                        null=True,
                        verbose_name="Title",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other"),
                        ],
                        default="other",
                        max_length=20,
                        verbose_name="Gender",
                    ),
                ),
                (
                    "street_number",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Street Number",
                    ),
                ),
                (
                    "suburb",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Suburb"
                    ),
                ),
                (
                    "zip_code",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="ZIP Code"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="City"
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="State / Province",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AF", "Afghanistan"),
                            ("AX", "Åland Islands"),
                            ("AL", "Albania"),
                            ("DZ", "Algeria"),
                            ("AS", "American Samoa"),
                            ("AD", "Andorra"),
                            ("AO", "Angola"),
                            ("AI", "Anguilla"),
                            ("AQ", "Antarctica"),
                            ("AG", "Antigua and Barbuda"),
                            ("AR", "Argentina"),
                            ("AM", "Armenia"),
                            ("AW", "Aruba"),
                            ("AU", "Australia"),
                            ("AT", "Austria"),
                            ("AZ", "Azerbaijan"),
                            ("BS", "Bahamas"),
                            ("BH", "Bahrain"),
                            ("BD", "Bangladesh"),
                            ("BB", "Barbados"),
                            ("BY", "Belarus"),
                            ("BE", "Belgium"),
                            ("BZ", "Belize"),
                            ("BJ", "Benin"),
                            ("BM", "Bermuda"),
                            ("BT", "Bhutan"),
                            ("BO", "Bolivia"),
                            ("BQ", "Bonaire, Sint Eustatius and Saba"),
                            ("BA", "Bosnia and Herzegovina"),
                            ("BW", "Botswana"),
                            ("BV", "Bouvet Island"),
                            ("BR", "Brazil"),
                            ("IO", "British Indian Ocean Territory"),
                            ("BN", "Brunei"),
                            ("BG", "Bulgaria"),
                            ("BF", "Burkina Faso"),
                            ("BI", "Burundi"),
                            ("CV", "Cabo Verde"),
                            ("KH", "Cambodia"),
                            ("CM", "Cameroon"),
                            ("CA", "Canada"),
                            ("KY", "Cayman Islands"),
                            ("CF", "Central African Republic"),
                            ("TD", "Chad"),
                            ("CL", "Chile"),
                            ("CN", "China"),
                            ("CX", "Christmas Island"),
                            ("CC", "Cocos (Keeling) Islands"),
                            ("CO", "Colombia"),
                            ("KM", "Comoros"),
                            ("CG", "Congo"),
                            ("CD", "Congo (the Democratic Republic of the)"),
                            ("CK", "Cook Islands"),
                            ("CR", "Costa Rica"),
                            ("CI", "Côte d'Ivoire"),
                            ("HR", "Croatia"),
                            ("CU", "Cuba"),
                            ("CW", "Curaçao"),
                            ("CY", "Cyprus"),
                            ("CZ", "Czechia"),
                            ("DK", "Denmark"),
                            ("DJ", "Djibouti"),
                            ("DM", "Dominica"),
                            ("DO", "Dominican Republic"),
                            ("EC", "Ecuador"),
                            ("EG", "Egypt"),
                            ("SV", "El Salvador"),
                            ("GQ", "Equatorial Guinea"),
                            ("ER", "Eritrea"),
                            ("EE", "Estonia"),
                            ("SZ", "Eswatini"),
                            ("ET", "Ethiopia"),
                            ("FK", "Falkland Islands (Malvinas)"),
                            ("FO", "Faroe Islands"),
                            ("FJ", "Fiji"),
                            ("FI", "Finland"),
                            ("FR", "France"),
                            ("GF", "French Guiana"),
                            ("PF", "French Polynesia"),
                            ("TF", "French Southern Territories"),
                            ("GA", "Gabon"),
                            ("GM", "Gambia"),
                            ("GE", "Georgia"),
                            ("DE", "Germany"),
                            ("GH", "Ghana"),
                            ("GI", "Gibraltar"),
                            ("GR", "Greece"),
                            ("GL", "Greenland"),
                            ("GD", "Grenada"),
                            ("GP", "Guadeloupe"),
                            ("GU", "Guam"),
                            ("GT", "Guatemala"),
                            ("GG", "Guernsey"),
                            ("GN", "Guinea"),
                            ("GW", "Guinea-Bissau"),
                            ("GY", "Guyana"),
                            ("HT", "Haiti"),
                            ("HM", "Heard Island and McDonald Islands"),
                            ("VA", "Holy See"),
                            ("HN", "Honduras"),
                            ("HK", "Hong Kong"),
                            ("HU", "Hungary"),
                            ("IS", "Iceland"),
                            ("IN", "India"),
                            ("ID", "Indonesia"),
                            ("IR", "Iran"),
                            ("IQ", "Iraq"),
                            ("IE", "Ireland"),
                            ("IM", "Isle of Man"),
                            ("IL", "Israel"),
                            ("IT", "Italy"),
                            ("JM", "Jamaica"),
                            ("JP", "Japan"),
                            ("JE", "Jersey"),
                            ("JO", "Jordan"),
                            ("KZ", "Kazakhstan"),
                            ("KE", "Kenya"),
                            ("KI", "Kiribati"),
                            ("KW", "Kuwait"),
                            ("KG", "Kyrgyzstan"),
                            ("LA", "Laos"),
                            ("LV", "Latvia"),
                            ("LB", "Lebanon"),
                            ("LS", "Lesotho"),
                            ("LR", "Liberia"),
                            ("LY", "Libya"),
                            ("LI", "Liechtenstein"),
                            ("LT", "Lithuania"),
                            ("LU", "Luxembourg"),
                            ("MO", "Macao"),
                            ("MG", "Madagascar"),
                            ("MW", "Malawi"),
                            ("MY", "Malaysia"),
                            ("MV", "Maldives"),
                            ("ML", "Mali"),
                            ("MT", "Malta"),
                            ("MH", "Marshall Islands"),
                            ("MQ", "Martinique"),
                            ("MR", "Mauritania"),
                            ("MU", "Mauritius"),
                            ("YT", "Mayotte"),
                            ("MX", "Mexico"),
                            ("FM", "Micronesia (Federated States of)"),
                            ("MD", "Moldova"),
                            ("MC", "Monaco"),
                            ("MN", "Mongolia"),
                            ("ME", "Montenegro"),
                            ("MS", "Montserrat"),
                            ("MA", "Morocco"),
                            ("MZ", "Mozambique"),
                            ("MM", "Myanmar"),
                            ("NA", "Namibia"),
                            ("NR", "Nauru"),
                            ("NP", "Nepal"),
                            ("NL", "Netherlands"),
                            ("NC", "New Caledonia"),
                            ("NZ", "New Zealand"),
                            ("NI", "Nicaragua"),
                            ("NE", "Niger"),
                            ("NG", "Nigeria"),
                            ("NU", "Niue"),
                            ("NF", "Norfolk Island"),
                            ("KP", "North Korea"),
                            ("MK", "North Macedonia"),
                            ("MP", "Northern Mariana Islands"),
                            ("NO", "Norway"),
                            ("OM", "Oman"),
                            ("PK", "Pakistan"),
                            ("PW", "Palau"),
                            ("PS", "Palestine, State of"),
                            ("PA", "Panama"),
                            ("PG", "Papua New Guinea"),
                            ("PY", "Paraguay"),
                            ("PE", "Peru"),
                            ("PH", "Philippines"),
                            ("PN", "Pitcairn"),
                            ("PL", "Poland"),
                            ("PT", "Portugal"),
                            ("PR", "Puerto Rico"),
                            ("QA", "Qatar"),
                            ("RE", "Réunion"),
                            ("RO", "Romania"),
                            ("RU", "Russia"),
                            ("RW", "Rwanda"),
                            ("BL", "Saint Barthélemy"),
                            ("SH", "Saint Helena, Ascension and Tristan da Cunha"),
                            ("KN", "Saint Kitts and Nevis"),
                            ("LC", "Saint Lucia"),
                            ("MF", "Saint Martin (French part)"),
                            ("PM", "Saint Pierre and Miquelon"),
                            ("VC", "Saint Vincent and the Grenadines"),
                            ("WS", "Samoa"),
                            ("SM", "San Marino"),
                            ("ST", "Sao Tome and Principe"),
                            ("SA", "Saudi Arabia"),
                            ("SN", "Senegal"),
                            ("RS", "Serbia"),
                            ("SC", "Seychelles"),
                            ("SL", "Sierra Leone"),
                            ("SG", "Singapore"),
                            ("SX", "Sint Maarten (Dutch part)"),
                            ("SK", "Slovakia"),
                            ("SI", "Slovenia"),
                            ("SB", "Solomon Islands"),
                            ("SO", "Somalia"),
                            ("ZA", "South Africa"),
                            ("GS", "South Georgia and the South Sandwich Islands"),
                            ("KR", "South Korea"),
                            ("SS", "South Sudan"),
                            ("ES", "Spain"),
                            ("LK", "Sri Lanka"),
                            ("SD", "Sudan"),
                            ("SR", "Suriname"),
                            ("SJ", "Svalbard and Jan Mayen"),
                            ("SE", "Sweden"),
                            ("CH", "Switzerland"),
                            ("SY", "Syria"),
                            ("TW", "Taiwan"),
                            ("TJ", "Tajikistan"),
                            ("TZ", "Tanzania"),
                            ("TH", "Thailand"),
                            ("TL", "Timor-Leste"),
                            ("TG", "Togo"),
                            ("TK", "Tokelau"),
                            ("TO", "Tonga"),
                            ("TT", "Trinidad and Tobago"),
                            ("TN", "Tunisia"),
                            ("TR", "Türkiye"),
                            ("TM", "Turkmenistan"),
                            ("TC", "Turks and Caicos Islands"),
                            ("TV", "Tuvalu"),
                            ("UG", "Uganda"),
                            ("UA", "Ukraine"),
                            ("AE", "United Arab Emirates"),
                            ("GB", "United Kingdom"),
                            ("UM", "United States Minor Outlying Islands"),
                            ("US", "United States of America"),
                            ("UY", "Uruguay"),
                            ("UZ", "Uzbekistan"),
                            ("VU", "Vanuatu"),
                            ("VE", "Venezuela"),
                            ("VN", "Vietnam"),
                            ("VG", "Virgin Islands (British)"),
                            ("VI", "Virgin Islands (U.S.)"),
                            ("WF", "Wallis and Futuna"),
                            ("EH", "Western Sahara"),
                            ("YE", "Yemen"),
                            ("ZM", "Zambia"),
                            ("ZW", "Zimbabwe"),
                            ("", "Select Country"),
                        ],
                        max_length=200,
                        null=True,
                        verbose_name="country",
                    ),
                ),
                (
                    "guarantor",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Guarantor"
                    ),
                ),
                (
                    "is_guarantor",
                    models.BooleanField(default=False, verbose_name="Is Guarantor"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("banned", "Banned"),
                            ("restricted", "Restricted"),
                            ("died", "Died"),
                        ],
                        default="active",
                        max_length=20,
                        verbose_name="Status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
                (
                    "ip_address",
                    models.GenericIPAddressField(
                        blank=True, null=True, verbose_name="IP Address"
                    ),
                ),
                ("device_details", models.TextField(blank=True, null=True)),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="branches.branch",
                        verbose_name="Branch",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
