# Singapore and Southeast Asian speech recognition dataset survey

Speech recognition datasets differ in setting, speakers, transcripts, access, and source recordings. These differences matter more than a single total-hours figure. This survey focuses on Singapore speech and identifies nearby regional collections. The [machine-readable inventory](data/dataset-inventory.csv) provides a source link and access note for each of 34 screened entries; related subsets are listed separately for clarity.

[Choose a dataset](#choose-by-task-and-evidence) · [Dataset map](#dataset-map) · [Examples](#what-the-data-looks-like) · [Shared sources](#shared-sources-and-subsets) · [Singapore datasets](#singapore-datasets-with-usable-asr-references) · [MNSC parts](#all-six-mnsc-asr-tests) · [Regional collections](#regional-and-code-switching-collections)

## Choose by task and evidence

“Reliable” has several meanings here. **Reference quality** describes who produced the transcript; it does not mean every word has been independently checked. **Coverage** asks whether the speakers and setting match your use case. **Access** asks whether the audio and its terms can be used as intended. **Independence** asks whether two reported results come from different original recordings. None of these is a single numerical quality score.

| Need | Best starting point | Confidence in published references | Constraint that matters most |
| --- | --- | --- | --- |
| Conversational Singapore English | [AppTek en-SG](#singapore-datasets-with-usable-asr-references) | Professional manual, verbatim annotation | Only ten speakers in role-played service calls; paired channels share calls. |
| Colloquial Singlish | [MNSC Part 3](#all-six-mnsc-asr-tests) | Published pre-annotated or human-edited references | Speaker labels and markup require a stated scoring convention; NSC derivatives are related. |
| Local names, food, places, brands | [MNSC Part 2](#all-six-mnsc-asr-tests) | Published references for prompted speech | Tests named entities in read prompts, not recognition in conversation. |
| Code-switched Singapore conversation | [MNSC Part 4](#all-six-mnsc-asr-tests) | Published references for mixed-language dialogue | Language mix and mixed-script scoring must be handled explicitly. |
| Singapore-accented web video | [GigaSpeechBench SGP-EN](#singapore-datasets-with-usable-asr-references) | Professional transcription and publisher quality checks | Audio-use terms are unclear; accent metadata does not prove speaker nationality. |
| Read Singapore-accented English | [Common Voice](#singapore-datasets-with-usable-asr-references) | Community-validated read-speech references | Test-split count and speaker balance depend on the exact release. |

AppTek offers the clearest combination of public test files, stated dataset licence, and manual transcripts for a conversational English study. MNSC Part 3 is more directly about spontaneous local speech. Use both if the question spans service calls and colloquial conversation; they represent different settings. GigaSpeechBench adds a different recording source, subject to resolving its audio terms. Do not treat SASRBench and MNSC Part 3 as independent confirmations: both derive from NSC Part 3. A claimed “unseen” test also needs evidence about each model's training data; different dataset names alone cannot establish that.

**Not ready as a straightforward WER reference:** YCSEP's released transcripts are automated; MERLIon CCS primarily documents language identification and diarization; NAS oral-history search text can be machine-generated; ICE-SIN and several historical corpora lack a clearly accessible, aligned ASR test. They remain useful for discovery or qualitative study. Licence uncertainty and transcript uncertainty are separate problems.

## Dataset map

Start with the speech setting you want to understand. These groups describe the main use of each source; a dataset may contain more than one style.

![Dataset categories: read speech and names, conversation, code-switching, and languages and styles](assets/dataset-map.svg?palette=dark)

The map describes content, not transcript reliability. For example, YCSEP contains natural speech but its automatic transcripts are unsuitable as an unchecked WER reference.

## What the data looks like

Short excerpts below preserve the published spelling and annotation. They illustrate reference formats, not model predictions or overall transcript quality. Follow the source links for context and available audio.

| Dataset and example | Reference excerpt | What to notice |
| --- | --- | --- |
| [MNSC Part 1, public viewer](https://huggingface.co/datasets/MERaLiON/Multitask-National-Speech-Corpus-v1/viewer/ASR-PART1-Test/train) | “we watched the drama unfold before our eyes” | A clean read sentence. Local accent is an audio property and cannot be judged from these words alone. |
| [SASRBench-v1, first displayed test record](https://huggingface.co/datasets/mjwong/SASRBench-v1/viewer/default/test) | “I don't know [eh] I going to Korea [ah]” | Local particles and colloquial grammar are retained. Bracket handling affects scoring. |
| [AppTek en-SG, agriculture call](https://huggingface.co/datasets/apptek-com/apptek_callcenter_dialogues/blob/b98967d9946f7f59f58d08624a2a00fe98fe0219/test/en-SG/metadata.jsonl) | “Okay lah we shared that with farmers people.” | A particle appears in a service-call transcript. Removing it changes the reference being evaluated. |
| [ASCEND, training record `00000`](https://huggingface.co/datasets/CAiRE/ASCEND/viewer/default/train) | “我刚刚开始record” | Mandarin and English appear in one phrase: approximately “I just started recording.” This is a Hong Kong training example. |

AppTek record: `en_SG_Agriculture_1586768_channel1.wav`. Excerpts are attributed to the linked publishers. AppTek and ASCEND state CC BY-SA 4.0; MNSC cites inherited Singapore Open Data Licence terms; SASRBench carries an MIT badge alongside its NSC provenance.

## Shared sources and subsets

Several releases reuse source material. Arrows below mean “supplies material to,” not “every test recording overlaps.” Exact overlap between MNSC Part 3 and SASRBench is not established.

![Selected source families feeding derived ASR datasets](assets/source-reuse.svg?palette=dark)

This is a selected relationship map, not the complete source list for either aggregate. Adding the hours of parent and derived releases would double-count material. AppTek and GigaSpeechBench have separately described collection processes; that alone does not establish exclusion from a particular model's training data.

## Singapore datasets with usable ASR references

| Dataset | Speech and size | Access and interpretation |
| --- | --- | --- |
| [AppTek Call-Center Dialogues en-SG](https://huggingface.co/datasets/apptek-com/apptek_callcenter_dialogues) | 57 paired, role-played customer-agent calls from 10 Singaporean speakers; 114 channel recordings; 8.1 annotated speech hours. | Public `test` split, professional verbatim transcripts, CC BY-SA 4.0. The two channels belong to the same calls. The [publisher's scorer](https://huggingface.co/datasets/apptek-com/apptek_callcenter_dialogues/blob/b98967d9946f7f59f58d08624a2a00fe98fe0219/score.py) omits unmatched files, and its [normalizer](https://huggingface.co/datasets/apptek-com/apptek_callcenter_dialogues/blob/b98967d9946f7f59f58d08624a2a00fe98fe0219/word_mappings.py) removes `lah` and `ah`. These choices affect Singapore English WER. |
| [GigaSpeechBench SGP-EN](https://github.com/SpeechColab/GigaSpeechBench) | Singapore-accented English from web video. Its public metadata has 45 parent recordings and 9,480 segments totaling 10.7539 segment hours; 9,032 exceed 0.5 seconds. | [Paper](https://arxiv.org/html/2606.28884v3) describes professional transcription. Accent labels do not establish each speaker's nationality. The dataset page does not state a data licence or per-clip audio rights. The full raw segment count differs from a scored subset after duration and text filters. |
| [SASRBench-v1](https://huggingface.co/datasets/mjwong/SASRBench-v1) | 3,747 conversational Singlish test clips, each selected for at least 10 words and at most 20 seconds. | Same-room close-talk speech derived from National Speech Corpus (NSC) Part 3. It is a different packaging of that source family from MNSC Part 3; exact clip overlap is not established. |
| [SG Streets](https://github.com/khassanoff/SG_streets) | Singapore street-name reading; [SEA-SpeechBench](https://huggingface.co/datasets/MERaLiON/sea_audiobench_datasets_ASR) includes a 492-example, roughly 0.7-hour subset. | The upstream work describes six sessions with interviewer and interviewee recordings. The benchmark's example count is not a speaker count. Upstream audio terms are unspecified in the aggregate card. |
| [Common Voice English, Singapore accent](https://commonvoice.mozilla.org/en/datasets) | Scripted read speech tagged with a Singapore accent. [CV26 release metadata](https://github.com/common-voice/cv-dataset/blob/main/datasets/scripted-speech/cv-corpus-26.0-2026-06-12.json) counts 4,722 such clips across all splits. | The Singapore-accent test count for this release is not established here. A separate [published accent test](https://aclanthology.org/2023.emnlp-main.444.pdf) has 477 clips/0.64 h in its small split and 2,967 clips/4.13 h in its full split; the small split is nested in the full split and heavily concentrated in one speaker. Mozilla's [platform terms](https://community.mozilladatacollective.com/faq-why-cant-i-re-host-or-share-common-voice-datasets-that-i-download-from-mdc/) restrict mirroring. |
| [IMDA2RareWordDataset](https://github.com/cyaaronk/IMDA2RareWordDataset) | Local road names and addresses; NSC-derived test manifests. | Repository supplies manifests rather than WAV files. Original NSC audio must be obtained separately. Its exact recording overlap with MNSC Part 2 or SG Streets is unknown. |

## All six MNSC ASR tests

The [MNSC paper](https://arxiv.org/html/2501.01034v2) and [dataset release](https://huggingface.co/datasets/MERaLiON/Multitask-National-Speech-Corpus-v1) distinguish six named ASR Test configurations. Each is internally packaged under a Hugging Face split called `train`; the configuration name carries its intended test role. Parts 1–2 are sentence level and Parts 3–6 are dialogue level. They total 10,000 examples, but share the NSC source family. The paper's Part 1–2 test-hour cells are malformed, so their durations are omitted.

| Part | Test examples | Speech setting |
| --- | ---: | --- |
| 1 | 3,000 | Phonetically balanced read English |
| 2 | 3,000 | Prompted Singapore names, food, places, and brands |
| 3 | 1,000; about 7.7 h | Spontaneous daily-life conversation |
| 4 | 1,000; about 7.3 h | English conversation with Mandarin, Malay, or Tamil code-switching |
| 5 | 1,000; about 6.9 h | Debate, finance, and emotional speaking styles |
| 6 | 1,000; about 6.8 h | Travel, restaurant, banking, insurance, and public-service scenarios |

MNSC also contains spoken question answering, dialogue summarization, and paralinguistic tasks. Those are separate tasks, not extra ASR tests. Shared NSC provenance does not itself prove that two tests reuse the same recording. The [original IMDA corpus](https://www.imda.gov.sg/how-we-can-help/national-speech-corpus) has separate registration and attribution requirements.

## Other Singapore sources

| Source | What it adds | Availability caveat |
| --- | --- | --- |
| [MERLIon CCS](https://github.com/MERLIon-Challenge/merlion-ccs-2023) | Over 30 annotated hours and 300 recordings of Singapore English–Mandarin child-directed speech, described in its [paper](https://www.isca-archive.org/interspeech_2023/chua23_interspeech.pdf). | Public challenge data were announced in 2024; lexical ASR references and release terms need checking. Challenge tasks center on language identification and diarization. |
| [NIE Corpus of Spoken Singapore English](https://videoweb.nie.edu.sg/phonetic/niecsse/index.htm) | Interviews with 46 Singapore speakers and five British comparison speakers; read and phonetic examples are also linked. | Research use with acknowledgement; no standard data licence or aligned ASR test set stated. British comparison speech should be identified separately. |
| [Lim Siew Hwee informal corpus](https://videoweb.nie.edu.sg/phonetic/lim-siew-hwee-corpus/index.htm) | Three friend conversations with local particles in transcripts. | Small, qualitative resource; its focal speakers also appear in NIECSSE. |
| [YCSEP Singapore podcasts](https://huggingface.co/datasets/stcoats/YCSEP_v1) | Large collection of natural podcast speech. | WhisperX transcripts were not manually corrected. Its MIT label conflicts with noncommercial-use prose. |
| [ICE-SIN](https://www.ice-corpora.uzh.ch/en/access.htm) and [GSSEC](https://www3.ntu.edu.sg/home/yytan/interspeech.pdf) | Historical Singapore English, including roughly eight hours of GSSEC conversation incorporated into ICE-SIN. | ICE-SIN's million-word figure includes written text. Aligned audio access and ASR splits are unclear. |
| [Singapore English CALL](https://www.researchgate.net/publication/228449974_The_development_of_a_Singapore_English_call_resource), [NESSI](https://uclouvain.be/en/research-institutes/ilc/cecl/nessi.html), [NAS oral history](https://www.nas.gov.sg/archivesonline/oral_history_interviews/) | Pronunciation learning, student interviews, and historical interviews respectively. | Release rights and ready aligned test references vary; NAS audio-search text is automatically generated for some records. |

## Regional and code-switching collections

| Source | Scope | Interpretation |
| --- | --- | --- |
| [SEA-SpeechBench ASR](https://huggingface.co/datasets/MERaLiON/sea_audiobench_datasets_ASR) | 26,863 examples, roughly 52.9 hours, 11 languages, 33 configurations. | An aggregate of upstream sources with differing terms, not one new corpus. Its evaluation configurations are packaged as `train`. Includes 1,000 Mandarin SgpCCSC and 992 Thai elderly examples. |
| [SEAME](https://catalog.ldc.upenn.edu/LDC2015S04) | Roughly 192 hours of Singapore/Malaysia Mandarin-English conversation across the whole release. | LDC access agreement; phase I and II transcript versions differ. The 192-hour figure is not a test-set duration. |
| [ASCEND](https://huggingface.co/datasets/CAiRE/ASCEND) | Hong Kong Mandarin-English conversation; 10.62 hours overall and 1,315 test utterances. | CC BY-SA 4.0. Geographic scope differs from Singapore. |
| [CS-Dialogue](https://huggingface.co/datasets/BAAI/CS-Dialogue) | Mainland Chinese Mandarin-English dialogue. Paper reports a 6,293-utterance, 16.74-hour test. | Pinned public test manifests list 6,257 rows; reconcile this difference. CC BY-NC-SA 4.0. Its mixed error rate counts Chinese characters and English words. |
| [Singapore code-switch ASR tests](https://www.isca-archive.org/interspeech_2025/nguyen25_interspeech.pdf) | Malay-English 11.61 h and Mandarin-Malay 7.46 h use generated dialogue text spoken by Singaporeans; Tamil-English 13.73 h assembles MUCS and IMDA Part 3 sentences. | Available by request; these are prompted or assembled tests, not spontaneous multilingual conversation. |
| [Revolab Malaysian public split](https://huggingface.co/datasets/Revolab/ASR-Benchmark-Public) | 820 Malay/English clips, about 2.2 h, with human-verified references. | Includes 52 TTS clips, singing, role-played telephony, 153 FLEURS clips, 141 Common Voice clips, and TUFS Malay material. Access conditions apply; CC BY 4.0 covers annotations while source audio rights vary. |
| [FLEURS](https://huggingface.co/datasets/google/fleurs) | Multilingual read speech with named train, development, and test splits. | Useful language coverage; read speech is a different setting from conversation. CC BY 4.0 upstream. |

The SEA-SpeechBench [source list](https://huggingface.co/datasets/MERaLiON/sea_audiobench_datasets_ASR#source-data) also names Bloom-Speech, MIG, Bud500, VietMed, Common Voice 21, ESD, MalCSC, SMalDuSC, OpenSLR, SFDuSC, LOTUS, and Thai Elderly Speech. These source families are nested in the aggregate. [SEACrowd](https://github.com/SEACrowd/seacrowd-datahub) offers further dataset discovery; each loaded corpus retains its own terms.

## Other related releases

| Release | Relationship to the datasets above |
| --- | --- |
| [Reprocessed Singapore NSC](https://huggingface.co/datasets/recursal/reprocessed_singapore_national_speech_corpus) | Alternative packaging of NSC recordings and transcripts; not a new recording source. Its transformations and splits need checking against MNSC. |
| [MCV_ACCENT Singapore test](https://github.com/csalt-research/accented-codebooks-asr) | The published Common Voice accent test described above; its small test is nested in the full test. |
| [AudioBench Singapore evaluations](https://github.com/AudioLLMs/AudioBench/blob/main/src/dataset.py) | Singapore-content and Singlish-emotion sets appear in the benchmark code, but their audio and references are private. |
| [EdAcc](https://www.research.ed.ac.uk/en/datasets/the-edinburgh-international-accents-of-english-corpus/) | Nearly 40 hours of conversational English accents; useful for broader accent work, but not a Singapore-specific test. |
| [Emotional Speech Dataset](https://github.com/HLTSingapore/Emotional-Speech-Data) | English and Mandarin read speech across emotions, also used inside SEA-SpeechBench. The creator requests a research-use licence form despite an MIT repository badge; Singapore speaker origin is not established. |

## Reading the counts

A corpus total, a named evaluation configuration, and a derived subset answer different questions. AppTek's 8.1 hours count annotated speech rather than both channels' playback time. GigaSpeechBench's raw segment hours differ from a filtered scored set. SEAME's 192 and ASCEND's 10.62 hours describe full corpora. Common Voice and SEA-SpeechBench contain nested subsets. Licensing and transcript quality are described from publisher sources unless stated otherwise; the table does not certify every audio file or resolve recording-level overlap.
