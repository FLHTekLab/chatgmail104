import click
import logging.config as logging_config
from chatgmail import config
from chatgmail.adapters import gmail
from chatgmail.adapters import orm

logging_config.dictConfig(config.logging_config)


# msg_id = '18fb8942e2590167'
# with open(f'.gmail/{msg_id}.html', 'r', encoding='utf-8') as file:
#     resume_104_html = file.read()
# candidate = orm.candidate_mapper(msg_id, resume_104_html)
# print(f'{candidate}')

def check_msg(msg_id: str):
    msg_html = gmail.read_msg_from_cache(msg_id)
    candidate = orm.candidate_mapper(msg_id, msg_html)
    click.echo(f'{msg_id}|{candidate.validate()}|{candidate}')
    # click.echo(f'{json.dumps(candidate.digest(), indent=2, ensure_ascii=False, default=str)}')
    candidate_md = candidate.to_markdown()
    click.echo(candidate_md)


if __name__ == '__main__':
    # msg_id = '18fb8942e2590167'
    msg_id = '190dd40f1508cfb5'
    # gml = gmail.GmailInbox()
    # msg = gml.get_msg_by_id(msg_id=msg_id)
    # gml.list_msg('104應徵履歷 OR 透過104轉寄履歷')

    check_msg(msg_id)
