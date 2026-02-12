# Integration tests for najia compile workflow

from najia.najia import Najia


def test_compile_workflow_with_bian_gua():
    """Test complete compile workflow with transformed hexagram"""
    params = [2, 2, 1, 2, 4, 2]  # Has dynamic lines
    gua = Najia(verbose=2).compile(params=params, date='2019-12-25 00:20')
    
    assert gua.data is not None
    assert gua.data['mark'] == '001000'
    assert gua.data['name'] == '地山谦'
    assert len(gua.data['shiy']) == 3  # (世, 应, 索引)
    assert gua.data['gong'] in ['乾', '兑', '离', '震', '巽', '坎', '艮', '坤']
    assert len(gua.data['qin6']) == 6
    assert len(gua.data['god6']) == 6
    
    # Verify transformed hexagram
    assert gua.data['bian'] is not None
    assert 'name' in gua.data['bian']
    assert 'mark' in gua.data['bian']
    assert 'qin6' in gua.data['bian']


def test_compile_workflow_without_bian_gua():
    """Test compile workflow without transformed hexagram (no dynamic lines)"""
    params = [1, 1, 1, 1, 1, 1]  # No dynamic lines (all 1s)
    gua = Najia(verbose=2).compile(params=params, date='2019-12-25 00:20')
    
    assert gua.data is not None
    assert gua.data['mark'] == '111111'
    assert gua.data['name'] == '乾为天'
    
    # Should not have transformed hexagram
    assert gua.data['bian'] is None


def test_render_workflow():
    """Test complete render workflow"""
    params = [2, 2, 1, 2, 4, 2]
    gua = Najia(verbose=2).compile(params=params, date='2019-12-25 00:20')
    output = gua.render()
    
    assert isinstance(output, str)
    assert len(output) > 0
    assert '地山谦' in output


def test_compile_with_guaci():
    """Test compile workflow with hexagram text"""
    params = [2, 2, 1, 2, 4, 2]
    gua = Najia(verbose=2).compile(params=params, date='2019-12-25 00:20', guaci=True)
    output = gua.render()
    
    # Should include hexagram text when guaci=True
    assert len(output) > 0


def test_compile_without_date():
    """Test compile workflow without date (should use current time)"""
    params = [2, 2, 1, 2, 4, 2]
    gua = Najia(verbose=2).compile(params=params)
    
    assert gua.data is not None
    assert 'solar' in gua.data
    assert 'lunar' in gua.data
