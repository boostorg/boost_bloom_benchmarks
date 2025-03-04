# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for six different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` to use its AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.98</td>
    <td align="right">5.28</td>
    <td align="right">3.70</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">10.27</td>
    <td align="right">9.84</td>
    <td align="right">15.72</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.74</td>
    <td align="right">4.13</td>
    <td align="right">4.10</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">4.83</td>
    <td align="right">5.05</td>
    <td align="right">5.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">15.50</td>
    <td align="right">14.35</td>
    <td align="right">16.59</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.48</td>
    <td align="right">4.58</td>
    <td align="right">4.61</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.44</td>
    <td align="right">7.72</td>
    <td align="right">7.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.10</td>
    <td align="right">17.91</td>
    <td align="right">15.86</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.13</td>
    <td align="right">5.10</td>
    <td align="right">5.19</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">8.84</td>
    <td align="right">12.37</td>
    <td align="right">13.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">25.23</td>
    <td align="right">22.63</td>
    <td align="right">16.40</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.14</td>
    <td align="right">5.69</td>
    <td align="right">5.69</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">10.97</td>
    <td align="right">14.67</td>
    <td align="right">14.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.75</td>
    <td align="right">3.05</td>
    <td align="right">3.10</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.53</td>
    <td align="right">4.77</td>
    <td align="right">4.73</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.19</td>
    <td align="right">5.89</td>
    <td align="right">6.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.30</td>
    <td align="right">2.91</td>
    <td align="right">2.91</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.09</td>
    <td align="right">5.14</td>
    <td align="right">5.15</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.63</td>
    <td align="right">9.14</td>
    <td align="right">9.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.52</td>
    <td align="right">5.55</td>
    <td align="right">3.80</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.95</td>
    <td align="right">5.99</td>
    <td align="right">5.99</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.69</td>
    <td align="right">13.21</td>
    <td align="right">13.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">5.49</td>
    <td align="right">5.53</td>
    <td align="right">3.77</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.47</td>
    <td align="right">6.35</td>
    <td align="right">6.35</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">11.55</td>
    <td align="right">16.50</td>
    <td align="right">16.46</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.46</td>
    <td align="right">17.60</td>
    <td align="right">8.08</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">13.16</td>
    <td align="right">12.79</td>
    <td align="right">17.28</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.78</td>
    <td align="right">5.43</td>
    <td align="right">5.48</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.13</td>
    <td align="right">7.01</td>
    <td align="right">7.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">21.68</td>
    <td align="right">19.34</td>
    <td align="right">18.38</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.90</td>
    <td align="right">7.29</td>
    <td align="right">8.00</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.00</td>
    <td align="right">9.88</td>
    <td align="right">9.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">29.43</td>
    <td align="right">34.41</td>
    <td align="right">19.37</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">15.89</td>
    <td align="right">10.54</td>
    <td align="right">7.62</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.65</td>
    <td align="right">17.42</td>
    <td align="right">15.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">47.46</td>
    <td align="right">42.99</td>
    <td align="right">19.70</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">10.57</td>
    <td align="right">11.30</td>
    <td align="right">16.92</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">16.06</td>
    <td align="right">22.45</td>
    <td align="right">21.62</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.63</td>
    <td align="right">4.21</td>
    <td align="right">4.22</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.90</td>
    <td align="right">6.06</td>
    <td align="right">6.09</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.65</td>
    <td align="right">8.12</td>
    <td align="right">8.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.95</td>
    <td align="right">3.79</td>
    <td align="right">3.76</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.18</td>
    <td align="right">6.28</td>
    <td align="right">6.25</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.18</td>
    <td align="right">9.94</td>
    <td align="right">9.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">9.15</td>
    <td align="right">9.06</td>
    <td align="right">6.31</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">8.01</td>
    <td align="right">7.96</td>
    <td align="right">8.00</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.99</td>
    <td align="right">15.56</td>
    <td align="right">15.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">9.86</td>
    <td align="right">9.82</td>
    <td align="right">6.99</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">11.06</td>
    <td align="right">10.93</td>
    <td align="right">9.96</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">18.08</td>
    <td align="right">24.36</td>
    <td align="right">23.90</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.70</td>
    <td align="right">4.02</td>
    <td align="right">3.79</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.22</td>
    <td align="right">9.22</td>
    <td align="right">15.38</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.32</td>
    <td align="right">4.05</td>
    <td align="right">3.97</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.04</td>
    <td align="right">3.58</td>
    <td align="right">3.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.72</td>
    <td align="right">13.48</td>
    <td align="right">16.47</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.84</td>
    <td align="right">4.57</td>
    <td align="right">4.73</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.71</td>
    <td align="right">3.36</td>
    <td align="right">3.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.39</td>
    <td align="right">16.67</td>
    <td align="right">15.77</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.35</td>
    <td align="right">5.09</td>
    <td align="right">5.09</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.51</td>
    <td align="right">6.35</td>
    <td align="right">6.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.42</td>
    <td align="right">21.18</td>
    <td align="right">15.26</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.82</td>
    <td align="right">5.87</td>
    <td align="right">5.85</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.82</td>
    <td align="right">6.89</td>
    <td align="right">6.90</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.56</td>
    <td align="right">2.50</td>
    <td align="right">2.49</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.87</td>
    <td align="right">4.69</td>
    <td align="right">4.57</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.24</td>
    <td align="right">3.53</td>
    <td align="right">3.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.18</td>
    <td align="right">2.26</td>
    <td align="right">2.25</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.60</td>
    <td align="right">5.33</td>
    <td align="right">5.34</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.71</td>
    <td align="right">3.71</td>
    <td align="right">3.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.18</td>
    <td align="right">4.37</td>
    <td align="right">3.17</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.93</td>
    <td align="right">6.02</td>
    <td align="right">6.00</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.85</td>
    <td align="right">6.09</td>
    <td align="right">6.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">4.13</td>
    <td align="right">4.35</td>
    <td align="right">3.14</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.83</td>
    <td align="right">3.33</td>
    <td align="right">3.36</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.29</td>
    <td align="right">7.01</td>
    <td align="right">7.21</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.43</td>
    <td align="right">15.45</td>
    <td align="right">6.51</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.15</td>
    <td align="right">10.83</td>
    <td align="right">16.57</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.02</td>
    <td align="right">4.79</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.69</td>
    <td align="right">4.36</td>
    <td align="right">4.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">16.13</td>
    <td align="right">15.49</td>
    <td align="right">17.40</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.15</td>
    <td align="right">5.20</td>
    <td align="right">5.65</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">4.33</td>
    <td align="right">4.34</td>
    <td align="right">4.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">20.65</td>
    <td align="right">27.37</td>
    <td align="right">18.02</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.73</td>
    <td align="right">6.64</td>
    <td align="right">7.85</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">8.44</td>
    <td align="right">7.97</td>
    <td align="right">8.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">43.40</td>
    <td align="right">42.56</td>
    <td align="right">18.01</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.11</td>
    <td align="right">8.90</td>
    <td align="right">10.98</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">8.83</td>
    <td align="right">13.11</td>
    <td align="right">11.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.21</td>
    <td align="right">3.14</td>
    <td align="right">3.28</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.81</td>
    <td align="right">5.64</td>
    <td align="right">5.44</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.85</td>
    <td align="right">4.31</td>
    <td align="right">4.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.52</td>
    <td align="right">2.68</td>
    <td align="right">2.67</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.74</td>
    <td align="right">6.32</td>
    <td align="right">5.88</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.43</td>
    <td align="right">4.96</td>
    <td align="right">4.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.40</td>
    <td align="right">5.81</td>
    <td align="right">4.26</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.79</td>
    <td align="right">9.07</td>
    <td align="right">9.99</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.23</td>
    <td align="right">8.01</td>
    <td align="right">9.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">10.08</td>
    <td align="right">9.57</td>
    <td align="right">5.59</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">4.84</td>
    <td align="right">8.12</td>
    <td align="right">5.98</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">9.15</td>
    <td align="right">11.54</td>
    <td align="right">10.73</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.37</td>
    <td align="right">7.98</td>
    <td align="right">5.46</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.64</td>
    <td align="right">7.28</td>
    <td align="right">16.31</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">2.25</td>
    <td align="right">1.81</td>
    <td align="right">1.75</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.33</td>
    <td align="right">4.06</td>
    <td align="right">2.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.89</td>
    <td align="right">9.20</td>
    <td align="right">15.84</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">2.23</td>
    <td align="right">2.01</td>
    <td align="right">1.96</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">4.37</td>
    <td align="right">3.15</td>
    <td align="right">2.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.32</td>
    <td align="right">10.04</td>
    <td align="right">16.51</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">3.04</td>
    <td align="right">2.69</td>
    <td align="right">2.31</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.38</td>
    <td align="right">3.43</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">25.69</td>
    <td align="right">17.45</td>
    <td align="right">16.77</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">3.52</td>
    <td align="right">3.25</td>
    <td align="right">2.68</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">8.47</td>
    <td align="right">6.02</td>
    <td align="right">7.80</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.43</td>
    <td align="right">2.46</td>
    <td align="right">4.83</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">2.34</td>
    <td align="right">1.83</td>
    <td align="right">1.83</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.87</td>
    <td align="right">2.12</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.12</td>
    <td align="right">2.39</td>
    <td align="right">2.41</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">2.28</td>
    <td align="right">1.85</td>
    <td align="right">2.06</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">6.27</td>
    <td align="right">3.75</td>
    <td align="right">3.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.67</td>
    <td align="right">3.19</td>
    <td align="right">3.03</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">3.24</td>
    <td align="right">3.89</td>
    <td align="right">2.66</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">8.59</td>
    <td align="right">3.57</td>
    <td align="right">4.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">6.18</td>
    <td align="right">5.05</td>
    <td align="right">3.31</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.20</td>
    <td align="right">2.46</td>
    <td align="right">2.06</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">7.40</td>
    <td align="right">5.69</td>
    <td align="right">5.35</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">37.05</td>
    <td align="right">20.12</td>
    <td align="right">12.87</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">18.09</td>
    <td align="right">16.12</td>
    <td align="right">26.61</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.16</td>
    <td align="right">6.19</td>
    <td align="right">7.25</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.54</td>
    <td align="right">7.04</td>
    <td align="right">5.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">46.39</td>
    <td align="right">36.65</td>
    <td align="right">31.99</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.69</td>
    <td align="right">9.74</td>
    <td align="right">10.84</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.02</td>
    <td align="right">14.01</td>
    <td align="right">12.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">68.01</td>
    <td align="right">54.68</td>
    <td align="right">33.66</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">15.53</td>
    <td align="right">12.03</td>
    <td align="right">13.39</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">23.71</td>
    <td align="right">18.49</td>
    <td align="right">18.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">95.45</td>
    <td align="right">72.08</td>
    <td align="right">32.50</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">15.96</td>
    <td align="right">12.95</td>
    <td align="right">14.75</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">33.94</td>
    <td align="right">32.68</td>
    <td align="right">29.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">6.25</td>
    <td align="right">10.01</td>
    <td align="right">9.26</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.61</td>
    <td align="right">6.08</td>
    <td align="right">6.25</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.02</td>
    <td align="right">8.63</td>
    <td align="right">6.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">8.89</td>
    <td align="right">9.47</td>
    <td align="right">9.97</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.97</td>
    <td align="right">10.95</td>
    <td align="right">12.14</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.87</td>
    <td align="right">16.31</td>
    <td align="right">15.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">19.66</td>
    <td align="right">17.78</td>
    <td align="right">12.44</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">12.70</td>
    <td align="right">12.06</td>
    <td align="right">11.53</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.54</td>
    <td align="right">15.72</td>
    <td align="right">15.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">13.53</td>
    <td align="right">15.84</td>
    <td align="right">10.63</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">10.14</td>
    <td align="right">9.70</td>
    <td align="right">9.35</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">20.61</td>
    <td align="right">18.35</td>
    <td align="right">18.87</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">35.10</td>
    <td align="right">5.81</td>
    <td align="right">3.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.00</td>
    <td align="right">12.50</td>
    <td align="right">16.99</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.82</td>
    <td align="right">4.22</td>
    <td align="right">4.26</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.89</td>
    <td align="right">5.58</td>
    <td align="right">5.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.39</td>
    <td align="right">17.67</td>
    <td align="right">17.63</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.96</td>
    <td align="right">4.73</td>
    <td align="right">4.74</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.61</td>
    <td align="right">8.51</td>
    <td align="right">8.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.96</td>
    <td align="right">21.39</td>
    <td align="right">16.81</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.62</td>
    <td align="right">5.32</td>
    <td align="right">5.27</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.26</td>
    <td align="right">10.93</td>
    <td align="right">10.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.16</td>
    <td align="right">27.17</td>
    <td align="right">17.49</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.91</td>
    <td align="right">6.08</td>
    <td align="right">5.91</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">17.91</td>
    <td align="right">14.28</td>
    <td align="right">14.21</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.34</td>
    <td align="right">3.93</td>
    <td align="right">3.93</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.98</td>
    <td align="right">5.30</td>
    <td align="right">5.23</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.17</td>
    <td align="right">5.58</td>
    <td align="right">5.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.88</td>
    <td align="right">4.87</td>
    <td align="right">4.10</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.03</td>
    <td align="right">6.02</td>
    <td align="right">5.85</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.33</td>
    <td align="right">8.75</td>
    <td align="right">7.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.98</td>
    <td align="right">7.11</td>
    <td align="right">5.37</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.29</td>
    <td align="right">6.54</td>
    <td align="right">6.54</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.85</td>
    <td align="right">10.51</td>
    <td align="right">10.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">4.91</td>
    <td align="right">7.15</td>
    <td align="right">5.38</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.34</td>
    <td align="right">7.48</td>
    <td align="right">7.38</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.97</td>
    <td align="right">12.90</td>
    <td align="right">13.81</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">42.72</td>
    <td align="right">21.17</td>
    <td align="right">7.75</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.61</td>
    <td align="right">13.14</td>
    <td align="right">17.68</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.00</td>
    <td align="right">4.73</td>
    <td align="right">4.54</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.44</td>
    <td align="right">6.35</td>
    <td align="right">6.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.75</td>
    <td align="right">19.28</td>
    <td align="right">18.61</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.08</td>
    <td align="right">5.28</td>
    <td align="right">5.28</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.18</td>
    <td align="right">10.47</td>
    <td align="right">10.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">34.23</td>
    <td align="right">26.44</td>
    <td align="right">18.14</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.54</td>
    <td align="right">7.54</td>
    <td align="right">10.14</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">25.03</td>
    <td align="right">16.08</td>
    <td align="right">18.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">67.06</td>
    <td align="right">71.22</td>
    <td align="right">22.08</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">16.89</td>
    <td align="right">13.46</td>
    <td align="right">13.84</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">29.43</td>
    <td align="right">24.60</td>
    <td align="right">25.78</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.64</td>
    <td align="right">4.22</td>
    <td align="right">4.24</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.91</td>
    <td align="right">5.67</td>
    <td align="right">5.67</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">12.10</td>
    <td align="right">6.36</td>
    <td align="right">6.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.67</td>
    <td align="right">5.71</td>
    <td align="right">4.50</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.14</td>
    <td align="right">6.86</td>
    <td align="right">6.87</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">19.51</td>
    <td align="right">10.93</td>
    <td align="right">10.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.31</td>
    <td align="right">10.75</td>
    <td align="right">9.23</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">14.15</td>
    <td align="right">17.63</td>
    <td align="right">13.66</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">24.20</td>
    <td align="right">14.11</td>
    <td align="right">14.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">14.97</td>
    <td align="right">17.52</td>
    <td align="right">13.72</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">18.67</td>
    <td align="right">16.33</td>
    <td align="right">16.04</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">29.82</td>
    <td align="right">19.63</td>
    <td align="right">20.87</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">60.45</td>
    <td align="right">31.64</td>
    <td align="right">16.78</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">26.99</td>
    <td align="right">41.40</td>
    <td align="right">36.24</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.44</td>
    <td align="right">16.15</td>
    <td align="right">15.94</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.14</td>
    <td align="right">20.38</td>
    <td align="right">20.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">36.83</td>
    <td align="right">63.22</td>
    <td align="right">39.11</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.49</td>
    <td align="right">19.42</td>
    <td align="right">19.24</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.28</td>
    <td align="right">26.68</td>
    <td align="right">26.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.34</td>
    <td align="right">77.07</td>
    <td align="right">37.99</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.27</td>
    <td align="right">18.53</td>
    <td align="right">18.44</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.85</td>
    <td align="right">33.14</td>
    <td align="right">33.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">56.32</td>
    <td align="right">96.18</td>
    <td align="right">37.40</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.18</td>
    <td align="right">18.79</td>
    <td align="right">18.80</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">35.08</td>
    <td align="right">37.55</td>
    <td align="right">37.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.47</td>
    <td align="right">13.51</td>
    <td align="right">13.51</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.04</td>
    <td align="right">19.70</td>
    <td align="right">19.71</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.46</td>
    <td align="right">22.05</td>
    <td align="right">22.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.79</td>
    <td align="right">16.47</td>
    <td align="right">15.86</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">15.90</td>
    <td align="right">18.64</td>
    <td align="right">18.63</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.29</td>
    <td align="right">28.91</td>
    <td align="right">28.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.46</td>
    <td align="right">19.39</td>
    <td align="right">19.44</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.00</td>
    <td align="right">18.55</td>
    <td align="right">18.25</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.69</td>
    <td align="right">45.78</td>
    <td align="right">45.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">24.06</td>
    <td align="right">25.48</td>
    <td align="right">25.46</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.87</td>
    <td align="right">19.93</td>
    <td align="right">20.01</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.58</td>
    <td align="right">55.33</td>
    <td align="right">55.43</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">70.95</td>
    <td align="right">105.15</td>
    <td align="right">20.64</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">27.37</td>
    <td align="right">42.56</td>
    <td align="right">39.18</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.75</td>
    <td align="right">16.07</td>
    <td align="right">16.16</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.47</td>
    <td align="right">20.59</td>
    <td align="right">20.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">35.79</td>
    <td align="right">60.85</td>
    <td align="right">39.98</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.21</td>
    <td align="right">19.65</td>
    <td align="right">19.32</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.12</td>
    <td align="right">25.23</td>
    <td align="right">25.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">42.76</td>
    <td align="right">74.18</td>
    <td align="right">38.20</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">17.07</td>
    <td align="right">18.63</td>
    <td align="right">18.51</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.49</td>
    <td align="right">33.12</td>
    <td align="right">33.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">56.35</td>
    <td align="right">94.82</td>
    <td align="right">37.71</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">18.23</td>
    <td align="right">20.63</td>
    <td align="right">19.39</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">35.37</td>
    <td align="right">38.90</td>
    <td align="right">38.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">10.70</td>
    <td align="right">13.75</td>
    <td align="right">13.75</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.27</td>
    <td align="right">19.85</td>
    <td align="right">19.84</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">32.84</td>
    <td align="right">22.53</td>
    <td align="right">22.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.54</td>
    <td align="right">16.42</td>
    <td align="right">15.51</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">15.98</td>
    <td align="right">18.79</td>
    <td align="right">18.73</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.09</td>
    <td align="right">29.09</td>
    <td align="right">29.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">14.48</td>
    <td align="right">19.03</td>
    <td align="right">18.86</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">17.82</td>
    <td align="right">18.57</td>
    <td align="right">18.21</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">64.62</td>
    <td align="right">46.88</td>
    <td align="right">47.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">24.97</td>
    <td align="right">26.53</td>
    <td align="right">26.43</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">19.78</td>
    <td align="right">20.50</td>
    <td align="right">21.89</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">80.73</td>
    <td align="right">57.19</td>
    <td align="right">57.74</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">63.35</td>
    <td align="right">12.85</td>
    <td align="right">8.42</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">13.79</td>
    <td align="right">23.09</td>
    <td align="right">26.61</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.52</td>
    <td align="right">12.32</td>
    <td align="right">12.32</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.76</td>
    <td align="right">16.04</td>
    <td align="right">16.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.52</td>
    <td align="right">35.45</td>
    <td align="right">29.33</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.18</td>
    <td align="right">14.05</td>
    <td align="right">14.10</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.27</td>
    <td align="right">22.42</td>
    <td align="right">22.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.79</td>
    <td align="right">47.45</td>
    <td align="right">30.11</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.61</td>
    <td align="right">15.46</td>
    <td align="right">15.48</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.12</td>
    <td align="right">32.21</td>
    <td align="right">32.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">32.38</td>
    <td align="right">60.76</td>
    <td align="right">30.32</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.55</td>
    <td align="right">16.32</td>
    <td align="right">16.31</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">30.20</td>
    <td align="right">37.11</td>
    <td align="right">37.12</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.01</td>
    <td align="right">9.38</td>
    <td align="right">9.43</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.77</td>
    <td align="right">13.93</td>
    <td align="right">13.90</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.28</td>
    <td align="right">16.78</td>
    <td align="right">16.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.01</td>
    <td align="right">14.01</td>
    <td align="right">13.99</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.54</td>
    <td align="right">15.36</td>
    <td align="right">15.37</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.84</td>
    <td align="right">22.51</td>
    <td align="right">22.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.85</td>
    <td align="right">17.63</td>
    <td align="right">17.65</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.64</td>
    <td align="right">16.79</td>
    <td align="right">16.79</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.68</td>
    <td align="right">30.86</td>
    <td align="right">30.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">17.16</td>
    <td align="right">22.06</td>
    <td align="right">22.04</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.92</td>
    <td align="right">17.89</td>
    <td align="right">17.92</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.99</td>
    <td align="right">35.89</td>
    <td align="right">35.86</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">76.52</td>
    <td align="right">46.98</td>
    <td align="right">11.22</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">14.13</td>
    <td align="right">22.90</td>
    <td align="right">28.42</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.66</td>
    <td align="right">12.56</td>
    <td align="right">12.57</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.08</td>
    <td align="right">16.66</td>
    <td align="right">16.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.24</td>
    <td align="right">34.63</td>
    <td align="right">29.95</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">11.87</td>
    <td align="right">13.73</td>
    <td align="right">13.73</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">16.79</td>
    <td align="right">21.53</td>
    <td align="right">21.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.16</td>
    <td align="right">47.07</td>
    <td align="right">30.23</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">13.44</td>
    <td align="right">14.81</td>
    <td align="right">14.81</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.77</td>
    <td align="right">32.84</td>
    <td align="right">32.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">31.80</td>
    <td align="right">61.99</td>
    <td align="right">32.96</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">14.52</td>
    <td align="right">15.78</td>
    <td align="right">15.79</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">29.90</td>
    <td align="right">36.89</td>
    <td align="right">36.85</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.18</td>
    <td align="right">9.45</td>
    <td align="right">9.43</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">11.85</td>
    <td align="right">13.93</td>
    <td align="right">13.96</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.28</td>
    <td align="right">17.57</td>
    <td align="right">17.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.14</td>
    <td align="right">13.81</td>
    <td align="right">13.78</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.23</td>
    <td align="right">14.84</td>
    <td align="right">14.84</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">17.78</td>
    <td align="right">21.72</td>
    <td align="right">21.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">12.98</td>
    <td align="right">16.48</td>
    <td align="right">16.49</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">14.21</td>
    <td align="right">16.15</td>
    <td align="right">16.14</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">25.49</td>
    <td align="right">30.99</td>
    <td align="right">30.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">16.36</td>
    <td align="right">21.40</td>
    <td align="right">21.20</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">15.47</td>
    <td align="right">17.48</td>
    <td align="right">17.37</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">33.09</td>
    <td align="right">35.25</td>
    <td align="right">35.27</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">41.22</td>
    <td align="right">8.59</td>
    <td align="right">6.65</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">54.75</td>
    <td align="right">52.12</td>
    <td align="right">36.05</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.16</td>
    <td align="right">17.29</td>
    <td align="right">20.45</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">20.03</td>
    <td align="right">39.81</td>
    <td align="right">39.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">84.16</td>
    <td align="right">78.93</td>
    <td align="right">39.84</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">20.41</td>
    <td align="right">18.90</td>
    <td align="right">21.17</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">24.69</td>
    <td align="right">58.63</td>
    <td align="right">56.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">104.63</td>
    <td align="right">96.29</td>
    <td align="right">38.40</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">21.36</td>
    <td align="right">19.13</td>
    <td align="right">20.41</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">36.12</td>
    <td align="right">77.54</td>
    <td align="right">77.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">133.40</td>
    <td align="right">121.47</td>
    <td align="right">40.22</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">23.58</td>
    <td align="right">20.59</td>
    <td align="right">21.16</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">41.73</td>
    <td align="right">92.56</td>
    <td align="right">92.80</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">16.25</td>
    <td align="right">23.51</td>
    <td align="right">23.54</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">21.58</td>
    <td align="right">22.40</td>
    <td align="right">24.79</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">22.79</td>
    <td align="right">40.44</td>
    <td align="right">40.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">16.01</td>
    <td align="right">32.46</td>
    <td align="right">23.64</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">23.87</td>
    <td align="right">23.78</td>
    <td align="right">25.72</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">29.21</td>
    <td align="right">57.02</td>
    <td align="right">57.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">26.57</td>
    <td align="right">54.34</td>
    <td align="right">38.86</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">25.90</td>
    <td align="right">26.06</td>
    <td align="right">26.83</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">41.72</td>
    <td align="right">76.35</td>
    <td align="right">80.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0262</td>
    <td align="right">24.90</td>
    <td align="right">52.46</td>
    <td align="right">36.10</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">27.07</td>
    <td align="right">28.90</td>
    <td align="right">28.84</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">46.92</td>
    <td align="right">91.32</td>
    <td align="right">92.90</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">72.10</td>
    <td align="right">37.97</td>
    <td align="right">12.33</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">62.34</td>
    <td align="right">58.38</td>
    <td align="right">40.30</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">19.65</td>
    <td align="right">18.14</td>
    <td align="right">22.61</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">21.97</td>
    <td align="right">40.46</td>
    <td align="right">40.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">92.12</td>
    <td align="right">85.21</td>
    <td align="right">42.88</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">22.54</td>
    <td align="right">19.37</td>
    <td align="right">22.17</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">28.29</td>
    <td align="right">60.70</td>
    <td align="right">58.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">126.02</td>
    <td align="right">112.02</td>
    <td align="right">42.81</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">24.71</td>
    <td align="right">20.76</td>
    <td align="right">22.53</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.41</td>
    <td align="right">80.19</td>
    <td align="right">80.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">189.29</td>
    <td align="right">178.77</td>
    <td align="right">51.51</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">35.39</td>
    <td align="right">31.14</td>
    <td align="right">27.76</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">48.01</td>
    <td align="right">101.07</td>
    <td align="right">100.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">16.75</td>
    <td align="right">28.26</td>
    <td align="right">28.33</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">23.65</td>
    <td align="right">24.11</td>
    <td align="right">27.79</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">25.11</td>
    <td align="right">41.32</td>
    <td align="right">41.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">16.44</td>
    <td align="right">38.08</td>
    <td align="right">28.25</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">26.18</td>
    <td align="right">28.15</td>
    <td align="right">28.92</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">32.75</td>
    <td align="right">60.15</td>
    <td align="right">61.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">30.70</td>
    <td align="right">65.50</td>
    <td align="right">52.84</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">29.67</td>
    <td align="right">30.37</td>
    <td align="right">35.90</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">47.27</td>
    <td align="right">80.35</td>
    <td align="right">82.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">37.10</td>
    <td align="right">76.31</td>
    <td align="right">56.65</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">38.82</td>
    <td align="right">38.11</td>
    <td align="right">39.40</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">55.28</td>
    <td align="right">100.23</td>
    <td align="right">99.93</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
