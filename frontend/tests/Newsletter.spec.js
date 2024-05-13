import { mount } from '@vue/test-utils'
import { describe, it, expect, vi } from 'vitest'
import NewsletterThree from '../src/components/NewsletterSection.vue'
import axios from 'axios'

// Mockowanie axios
vi.mock('axios')

describe('NewsletterThree.vue', () => {
  it('renders correctly', () => {
    const wrapper = mount(NewsletterThree)
    expect(wrapper.find('h3').text()).toBe(wrapper.vm.text.title)
  })

  it('submits the form successfully', async () => {
    // Mockowanie odpowiedzi axios
    axios.post.mockResolvedValue({ ok: true })

    const wrapper = mount(NewsletterThree)

    // Ustawianie wartości inputów
    await wrapper.find('input[name="name"]').setValue('John Doe')
    await wrapper.find('input[name="email"]').setValue('john@example.com')

    // Symulowanie submit
    await wrapper.find('form').trigger('submit.prevent')

    // Sprawdzanie wyświetlania komunikatu
    expect(wrapper.find('.subscribe-message').exists()).toBe(true)
    expect(wrapper.find('.subscribe-message').text()).toBe('Zapisano do newslettera.')

  })

  it('handles form submission failure', async () => {
    // Mockowanie niepowodzenia axios
    axios.post.mockRejectedValue(new Error('Network Error'))

    const wrapper = mount(NewsletterThree)

    // Ustawianie wartości inputów
    await wrapper.find('input[name="name"]').setValue('Jane Doe')
    await wrapper.find('input[name="email"]').setValue('jane@example.com')

    // Symulowanie submit
    await wrapper.find('form').trigger('submit.prevent')

    // Sprawdzanie wyświetlania komunikatu
    expect(wrapper.find('.subscribe-message').exists()).toBe(true)
    expect(wrapper.find('.subscribe-message').text()).toBe('Zapisano do newslettera.')
  })
})
