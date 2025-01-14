expected_output = {
    'vrf':{
        'default':{
            'vrf_id':'0',
            'route_source':{
                'connected':{
                    'networks':7,
                    'overhead':1344,
                    'memory_bytes':1512
                },
                'local':{
                    'networks':8,
                    'overhead':1536,
                    'memory_bytes':1728
                },
                'ND':{
                    'networks':0,
                    'overhead':0,
                    'memory_bytes':0,
                    'default':0,
                    'prefix':0,
                    'destination':0,
                    'redirect':0
                },
                'ospf':{
                    '200':{
                        'networks':500,
                        'overhead':96000,
                        'memory_bytes':108000,
                        'intra_area':500,
                        'inter_area':0,
                        'external_1':0,
                        'external_2':0,
                        'nssa_external_1':0,
                        'nssa_external_2':0
                    },
                    '100':{
                        'networks':0,
                        'overhead':0,
                        'memory_bytes':0,
                        'intra_area':0,
                        'inter_area':0,
                        'external_1':0,
                        'external_2':0,
                        'nssa_external_1':0,
                        'nssa_external_2':0
                    },
                    '702':{
                        'networks':11,
                        'overhead':2112,
                        'memory_bytes':2376,
                        'intra_area':11,
                        'inter_area':0,
                        'external_1':0,
                        'external_2':0,
                        'nssa_external_1':0,
                        'nssa_external_2':0
                    },
                    '99':{
                        'networks':0,
                        'overhead':0,
                        'memory_bytes':0,
                        'intra_area':0,
                        'inter_area':0,
                        'external_1':0,
                        'external_2':0,
                        'nssa_external_1':0,
                        'nssa_external_2':0
                    },
                    '202':{
                        'networks':0,
                        'overhead':0,
                        'memory_bytes':0,
                        'intra_area':0,
                        'inter_area':0,
                        'external_1':0,
                        'external_2':0,
                        'nssa_external_1':0,
                        'nssa_external_2':0
                    }
                },
                'bgp':{
                    '65001':{
                        'networks':0,
                        'overhead':0,
                        'memory_bytes':0,
                        'external':0,
                        'internal':0,
                        'local':0
                    }
                },
                'static':{
                    'networks':0,
                    'overhead':0,
                    'memory_bytes':0,
                    'static':0,
                    'per_user_static':0
                }
            },
            'maximum_paths':16,
            'total_route_source':{
                'networks':526,
                'overhead':100992,
                'memory_bytes':113616
            },
            'number_of_prefixes':{
                'prefix_8':1,
                'prefix_64':8,
                'prefix_128':517
            }
        }
    }
}
