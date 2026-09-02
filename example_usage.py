from client import AutomatedRedTeamingAdversarialProbeClient

def main():
    client = AutomatedRedTeamingAdversarialProbeClient()
    res = client.run_adversarial_safety_probe('https://api.agent.ai', 'INDIRECT_INJECTION')
    print('Automated Red Teaming Probe: ' + res['red_team_probe_id'] + ' (Robustness: ' + str(res['system_robustness_score_pct']) + '%)')
    print('Probes Dispatched: ' + str(res['probes_dispatched_count']) + ' | Vulnerabilities: ' + str(res['jailbreak_vulnerabilities_found_count']))
    print('Attack Coverage: ' + ', '.join(res['attack_taxonomy_coverage']))
    print('Audit Dossier: ' + res['red_team_audit_dossier_url'])

if __name__ == '__main__':
    main()
