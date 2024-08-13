import valo_api
from datetime import datetime, timezone
from pprint import pprint

API_KEY = "HDEV-4f1a91a3-1953-45e5-aaf3-866947ea3769" # hide with Docker config
valo_api.set_api_key(API_KEY)


def generate_player_accts(name = 'Miraie', tag = '871'):
    """
    Call the wrapper API to gather account information relating to a player.
    Params:
        name: str
        tag: str
    """
    PlayerAccount = valo_api.get_account_details_by_name_v1(name, tag)
    if not PlayerAccount:
        return None
    return {
        'puuid': PlayerAccount.puuid,
        'region': PlayerAccount.region,
        'account_lvl': PlayerAccount.account_level,
        'name': PlayerAccount.name,
        'tag': PlayerAccount.tag,
        'acct_card_id': PlayerAccount.card.id,
        'acct_card_small': PlayerAccount.card.small,
        'acct_card_large': PlayerAccount.card.large,
        'acct_card_wide': PlayerAccount.card.wide,
        'last_update_raw': PlayerAccount.last_update_raw,
        'extract_timestamp_est': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def generate_lifetime_matches(puuid, region):
    lifetime_matches_list = valo_api.get_lifetime_matches_by_puuid_v1(puuid = puuid, region = region)
    if not lifetime_matches_list:
        return None
    return [
        {
            'map_name': match.meta.map.name,
            'map_id': match.meta.map.id,
            'map_version': match.meta.version,
            'match_started_at': match.meta.started_at,
            'season_id': match.meta.season.id,
            'season_short': match.meta.season.short,
            'cluster': match.meta.cluster,
            'region': match.meta.region,
            'game_mode': match.meta.mode,
            'puuid': match.stats.puuid,
            'team': match.stats.team,
            'level': match.stats.level,
            'character_id': match.stats.character.id,
            'character_name': match.stats.character.name,
            'tier': match.stats.tier,
            'score': match.stats.score,
            'kills': match.stats.kills,
            'deaths': match.stats.deaths,
            'assists': match.stats.assists,
            'headshots': match.stats.shots.head,
            'bodyshots': match.stats.shots.body,
            'legshots': match.stats.shots.leg,
            'damage_made': match.stats.damage.made,
            'damage_received': match.stats.damage.received,
            'red_team_score': match.teams.red,
            'blue_team_score': match.teams.blue
        }
        for match in lifetime_matches_list
    ]


if __name__ == "__main__":
    player_data = generate_player_accts()
    lifetime_matches = generate_lifetime_matches(player_data['puuid'], player_data['region'])
    pprint(lifetime_matches)