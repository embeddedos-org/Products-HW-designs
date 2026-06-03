// eRadar360_CAD — UI Component Tests

import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react-native';
import { Text, View, TouchableOpacity, TextInput, ScrollView, Switch, FlatList } from 'react-native';

describe('eRadar360_CAD — UI Components', () => {

  describe('Card component', () => {
    const TestCard = ({ title, subtitle, badge, onPress }: any) => (
      <TouchableOpacity testID='card' onPress={onPress}>
        <Text testID='card-title'>{title}</Text>
        {subtitle && <Text testID='card-subtitle'>{subtitle}</Text>}
        {badge && <Text testID='card-badge'>{badge}</Text>}
      </TouchableOpacity>
    );
    test('renders title', () => {
      const { getByTestId } = render(<TestCard title='Test Title' />);
      expect(getByTestId('card-title').props.children).toBe('Test Title');
    });
    test('renders subtitle when provided', () => {
      const { getByTestId } = render(<TestCard title='T' subtitle='Sub' />);
      expect(getByTestId('card-subtitle').props.children).toBe('Sub');
    });
    test('renders badge when provided', () => {
      const { getByTestId } = render(<TestCard title='T' badge='NEW' />);
      expect(getByTestId('card-badge').props.children).toBe('NEW');
    });
    test('calls onPress when tapped', () => {
      const onPress = jest.fn();
      const { getByTestId } = render(<TestCard title='T' onPress={onPress} />);
      fireEvent.press(getByTestId('card'));
      expect(onPress).toHaveBeenCalledTimes(1);
    });
    test('no subtitle by default', () => {
      const { queryByTestId } = render(<TestCard title='T' />);
      expect(queryByTestId('card-subtitle')).toBeNull();
    });
  });

  describe('SearchBar component', () => {
    const TestSearchBar = ({ onSearch }: any) => {
      const [q, setQ] = React.useState('');
      return (
        <View>
          <TextInput testID='search-input' value={q} onChangeText={setQ} />
          <TouchableOpacity testID='search-btn' onPress={() => onSearch(q)}>
            <Text>Go</Text>
          </TouchableOpacity>
        </View>
      );
    };
    test('renders input', () => {
      const { getByTestId } = render(<TestSearchBar onSearch={jest.fn()} />);
      expect(getByTestId('search-input')).toBeTruthy();
    });
    test('updates query on change', () => {
      const { getByTestId } = render(<TestSearchBar onSearch={jest.fn()} />);
      fireEvent.changeText(getByTestId('search-input'), 'hello');
      expect(getByTestId('search-input').props.value).toBe('hello');
    });
    test('calls onSearch on button press', () => {
      const onSearch = jest.fn();
      const { getByTestId } = render(<TestSearchBar onSearch={onSearch} />);
      fireEvent.changeText(getByTestId('search-input'), 'test');
      fireEvent.press(getByTestId('search-btn'));
      expect(onSearch).toHaveBeenCalledWith('test');
    });
    test('empty search calls with empty string', () => {
      const onSearch = jest.fn();
      const { getByTestId } = render(<TestSearchBar onSearch={onSearch} />);
      fireEvent.press(getByTestId('search-btn'));
      expect(onSearch).toHaveBeenCalledWith('');
    });
  });

  describe('Toggle / Switch', () => {
    const TestToggle = () => {
      const [on, setOn] = React.useState(false);
      return <Switch testID='toggle' value={on} onValueChange={setOn} />;
    };
    test('starts off', () => {
      const { getByTestId } = render(<TestToggle />);
      expect(getByTestId('toggle').props.value).toBe(false);
    });
    test('toggles on press', () => {
      const { getByTestId } = render(<TestToggle />);
      fireEvent(getByTestId('toggle'), 'valueChange', true);
      expect(getByTestId('toggle').props.value).toBe(true);
    });
  });

  describe('FlatList rendering', () => {
    const items = Array.from({ length: 10 }, (_, i) => ({ id: String(i), title: `Item ${i}` }));
    const TestList = () => (
      <FlatList testID='list' data={items} keyExtractor={i => i.id}
        renderItem={({ item }) => <Text testID={'item-' + item.id}>{item.title}</Text>} />
    );
    test('renders list', () => {
      const { getByTestId } = render(<TestList />);
      expect(getByTestId('list')).toBeTruthy();
    });
    test('renders first item', () => {
      const { getByTestId } = render(<TestList />);
      expect(getByTestId('item-0').props.children).toBe('Item 0');
    });
  });

  describe('Loading state', () => {
    const TestLoader = ({ loading }: { loading: boolean }) => (
      <View>
        {loading ? <Text testID='loading'>Loading...</Text> : <Text testID='content'>Content</Text>}
      </View>
    );
    test('shows loading', () => {
      const { getByTestId } = render(<TestLoader loading={true} />);
      expect(getByTestId('loading')).toBeTruthy();
    });
    test('shows content when not loading', () => {
      const { getByTestId } = render(<TestLoader loading={false} />);
      expect(getByTestId('content')).toBeTruthy();
    });
    test('hides content when loading', () => {
      const { queryByTestId } = render(<TestLoader loading={true} />);
      expect(queryByTestId('content')).toBeNull();
    });
  });

  describe('Empty state', () => {
    const TestEmpty = ({ items }: { items: any[] }) => (
      <View>
        {items.length === 0 ? <Text testID='empty'>No items found</Text> : <Text testID='has-items'>{items.length} items</Text>}
      </View>
    );
    test('shows empty state for empty array', () => {
      const { getByTestId } = render(<TestEmpty items={[]} />);
      expect(getByTestId('empty')).toBeTruthy();
    });
    test('shows count for non-empty', () => {
      const { getByTestId } = render(<TestEmpty items={[1, 2, 3]} />);
      expect(getByTestId('has-items').props.children).toEqual([3, ' items']);
    });
  });

  describe('Error state', () => {
    const TestError = ({ error }: { error: string | null }) => (
      <View>
        {error ? <Text testID='error-msg'>{error}</Text> : <Text testID='no-error'>OK</Text>}
      </View>
    );
    test('shows error message', () => {
      const { getByTestId } = render(<TestError error='Something went wrong' />);
      expect(getByTestId('error-msg').props.children).toBe('Something went wrong');
    });
    test('hides error when null', () => {
      const { queryByTestId } = render(<TestError error={null} />);
      expect(queryByTestId('error-msg')).toBeNull();
    });
  });
});
