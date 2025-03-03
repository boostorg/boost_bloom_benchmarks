# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for six different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; for Visual Studio builds,
`/arch:AVX2` is set, which causes `fast_multiblock32` to use its AVX2 variant.

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
    <td align="right">27.21</td>
    <td align="right">4.40</td>
    <td align="right">3.42</td>
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
    <td align="right">11.12</td>
    <td align="right">10.78</td>
    <td align="right">16.63</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.04</td>
    <td align="right">4.23</td>
    <td align="right">4.32</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">6.04</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">17.29</td>
    <td align="right">15.87</td>
    <td align="right">17.44</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.08</td>
    <td align="right">8.89</td>
    <td align="right">8.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.38</td>
    <td align="right">19.06</td>
    <td align="right">16.48</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.42</td>
    <td align="right">5.33</td>
    <td align="right">5.45</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.19</td>
    <td align="right">13.80</td>
    <td align="right">13.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">27.51</td>
    <td align="right">24.12</td>
    <td align="right">16.90</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.29</td>
    <td align="right">6.16</td>
    <td align="right">5.94</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">12.33</td>
    <td align="right">15.79</td>
    <td align="right">15.79</td>
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
    <td align="right">2.7421</td>
    <td align="right">8.01</td>
    <td align="right">10.52</td>
    <td align="right">10.82</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.87</td>
    <td align="right">5.04</td>
    <td align="right">5.04</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">6.19</td>
    <td align="right">5.75</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">3.76</td>
    <td align="right">4.83</td>
    <td align="right">4.83</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.49</td>
    <td align="right">5.57</td>
    <td align="right">5.57</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">11.73</td>
    <td align="right">9.08</td>
    <td align="right">9.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">17.15</td>
    <td align="right">10.47</td>
    <td align="right">8.35</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.27</td>
    <td align="right">6.27</td>
    <td align="right">6.31</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">11.51</td>
    <td align="right">11.91</td>
    <td align="right">11.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">9.25</td>
    <td align="right">10.56</td>
    <td align="right">6.13</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.74</td>
    <td align="right">6.72</td>
    <td align="right">6.73</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">13.60</td>
    <td align="right">14.65</td>
    <td align="right">14.64</td>
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
    <td align="right">30.61</td>
    <td align="right">17.22</td>
    <td align="right">7.22</td>
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
    <td align="right">13.07</td>
    <td align="right">12.10</td>
    <td align="right">17.24</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.66</td>
    <td align="right">4.82</td>
    <td align="right">4.91</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.10</td>
    <td align="right">6.75</td>
    <td align="right">6.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">20.04</td>
    <td align="right">18.72</td>
    <td align="right">18.24</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.75</td>
    <td align="right">6.12</td>
    <td align="right">7.04</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.27</td>
    <td align="right">9.73</td>
    <td align="right">9.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">29.13</td>
    <td align="right">26.83</td>
    <td align="right">18.32</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.57</td>
    <td align="right">8.15</td>
    <td align="right">8.24</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">15.19</td>
    <td align="right">15.79</td>
    <td align="right">16.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">59.51</td>
    <td align="right">57.31</td>
    <td align="right">20.99</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.69</td>
    <td align="right">13.48</td>
    <td align="right">10.65</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">20.58</td>
    <td align="right">25.38</td>
    <td align="right">24.29</td>
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
    <td align="right">2.7269</td>
    <td align="right">8.21</td>
    <td align="right">10.67</td>
    <td align="right">10.70</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.69</td>
    <td align="right">5.95</td>
    <td align="right">5.83</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.39</td>
    <td align="right">6.78</td>
    <td align="right">6.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">4.32</td>
    <td align="right">5.59</td>
    <td align="right">5.37</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.31</td>
    <td align="right">6.21</td>
    <td align="right">6.84</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">13.32</td>
    <td align="right">10.22</td>
    <td align="right">10.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">22.16</td>
    <td align="right">14.78</td>
    <td align="right">10.86</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">8.89</td>
    <td align="right">8.84</td>
    <td align="right">9.12</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">14.54</td>
    <td align="right">15.08</td>
    <td align="right">14.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">17.56</td>
    <td align="right">18.85</td>
    <td align="right">15.40</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">14.82</td>
    <td align="right">12.06</td>
    <td align="right">14.86</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">24.58</td>
    <td align="right">23.67</td>
    <td align="right">25.02</td>
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
    <td align="right">26.72</td>
    <td align="right">4.63</td>
    <td align="right">3.75</td>
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
    <td align="right">8.66</td>
    <td align="right">8.16</td>
    <td align="right">14.69</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.16</td>
    <td align="right">3.73</td>
    <td align="right">3.73</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.06</td>
    <td align="right">5.27</td>
    <td align="right">5.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.69</td>
    <td align="right">12.74</td>
    <td align="right">16.11</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.69</td>
    <td align="right">4.37</td>
    <td align="right">4.37</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.00</td>
    <td align="right">8.21</td>
    <td align="right">8.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.52</td>
    <td align="right">15.62</td>
    <td align="right">15.32</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.28</td>
    <td align="right">4.97</td>
    <td align="right">4.98</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.13</td>
    <td align="right">12.50</td>
    <td align="right">12.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.70</td>
    <td align="right">19.61</td>
    <td align="right">15.72</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.76</td>
    <td align="right">5.59</td>
    <td align="right">5.76</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">13.53</td>
    <td align="right">12.96</td>
    <td align="right">12.95</td>
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
    <td align="right">2.7421</td>
    <td align="right">3.30</td>
    <td align="right">3.95</td>
    <td align="right">3.95</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.73</td>
    <td align="right">4.34</td>
    <td align="right">4.34</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">4.76</td>
    <td align="right">5.13</td>
    <td align="right">5.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">2.72</td>
    <td align="right">3.53</td>
    <td align="right">3.51</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.33</td>
    <td align="right">5.28</td>
    <td align="right">5.08</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.15</td>
    <td align="right">8.42</td>
    <td align="right">8.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">10.55</td>
    <td align="right">6.11</td>
    <td align="right">4.66</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.89</td>
    <td align="right">5.90</td>
    <td align="right">5.90</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">10.29</td>
    <td align="right">13.14</td>
    <td align="right">12.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">5.95</td>
    <td align="right">6.72</td>
    <td align="right">4.44</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">5.38</td>
    <td align="right">6.31</td>
    <td align="right">6.32</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">14.20</td>
    <td align="right">14.62</td>
    <td align="right">14.60</td>
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
    <td align="right">31.58</td>
    <td align="right">16.73</td>
    <td align="right">6.25</td>
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
    <td align="right">11.33</td>
    <td align="right">11.06</td>
    <td align="right">16.64</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.08</td>
    <td align="right">4.73</td>
    <td align="right">4.74</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.06</td>
    <td align="right">7.36</td>
    <td align="right">7.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.63</td>
    <td align="right">16.09</td>
    <td align="right">17.70</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.54</td>
    <td align="right">5.19</td>
    <td align="right">5.26</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">10.26</td>
    <td align="right">10.69</td>
    <td align="right">10.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">23.62</td>
    <td align="right">25.49</td>
    <td align="right">17.95</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.03</td>
    <td align="right">6.70</td>
    <td align="right">7.31</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.55</td>
    <td align="right">17.89</td>
    <td align="right">17.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">34.85</td>
    <td align="right">31.82</td>
    <td align="right">17.36</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">7.53</td>
    <td align="right">7.31</td>
    <td align="right">7.49</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">17.27</td>
    <td align="right">16.67</td>
    <td align="right">17.33</td>
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
    <td align="right">2.7269</td>
    <td align="right">4.44</td>
    <td align="right">5.25</td>
    <td align="right">5.21</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.74</td>
    <td align="right">5.48</td>
    <td align="right">5.48</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.16</td>
    <td align="right">7.24</td>
    <td align="right">7.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">3.47</td>
    <td align="right">4.36</td>
    <td align="right">4.40</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.28</td>
    <td align="right">6.20</td>
    <td align="right">6.05</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.48</td>
    <td align="right">10.65</td>
    <td align="right">10.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">10.89</td>
    <td align="right">7.80</td>
    <td align="right">6.06</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">5.94</td>
    <td align="right">7.05</td>
    <td align="right">7.02</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">12.46</td>
    <td align="right">16.02</td>
    <td align="right">14.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">8.26</td>
    <td align="right">8.96</td>
    <td align="right">6.50</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.02</td>
    <td align="right">8.79</td>
    <td align="right">8.13</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.73</td>
    <td align="right">18.09</td>
    <td align="right">17.97</td>
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
    <td align="right">21.49</td>
    <td align="right">4.40</td>
    <td align="right">3.95</td>
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
    <td align="right">7.52</td>
    <td align="right">5.08</td>
    <td align="right">12.57</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.45</td>
    <td align="right">1.71</td>
    <td align="right">1.31</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.49</td>
    <td align="right">1.90</td>
    <td align="right">1.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.01</td>
    <td align="right">7.40</td>
    <td align="right">13.10</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.56</td>
    <td align="right">1.51</td>
    <td align="right">1.45</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.26</td>
    <td align="right">2.11</td>
    <td align="right">2.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">15.12</td>
    <td align="right">9.53</td>
    <td align="right">12.34</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.93</td>
    <td align="right">1.89</td>
    <td align="right">1.84</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.56</td>
    <td align="right">3.17</td>
    <td align="right">3.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.62</td>
    <td align="right">12.27</td>
    <td align="right">11.80</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">3.75</td>
    <td align="right">2.35</td>
    <td align="right">2.03</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">4.88</td>
    <td align="right">3.80</td>
    <td align="right">9.00</td>
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
    <td align="right">2.27</td>
    <td align="right">2.00</td>
    <td align="right">1.98</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.71</td>
    <td align="right">1.52</td>
    <td align="right">1.41</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.07</td>
    <td align="right">2.00</td>
    <td align="right">2.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.68</td>
    <td align="right">1.59</td>
    <td align="right">1.45</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.81</td>
    <td align="right">1.48</td>
    <td align="right">1.46</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.94</td>
    <td align="right">2.39</td>
    <td align="right">3.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.47</td>
    <td align="right">3.82</td>
    <td align="right">2.52</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.98</td>
    <td align="right">1.97</td>
    <td align="right">1.80</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.59</td>
    <td align="right">3.27</td>
    <td align="right">3.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">3.28</td>
    <td align="right">3.67</td>
    <td align="right">2.24</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.99</td>
    <td align="right">1.81</td>
    <td align="right">1.80</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.42</td>
    <td align="right">4.48</td>
    <td align="right">4.35</td>
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
    <td align="right">30.45</td>
    <td align="right">14.71</td>
    <td align="right">9.84</td>
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
    <td align="right">10.75</td>
    <td align="right">13.62</td>
    <td align="right">20.79</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.56</td>
    <td align="right">5.51</td>
    <td align="right">5.49</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.35</td>
    <td align="right">5.72</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">30.16</td>
    <td align="right">30.68</td>
    <td align="right">26.13</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">7.16</td>
    <td align="right">8.24</td>
    <td align="right">8.03</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">9.85</td>
    <td align="right">11.44</td>
    <td align="right">12.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">55.00</td>
    <td align="right">40.90</td>
    <td align="right">25.43</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.84</td>
    <td align="right">10.15</td>
    <td align="right">9.42</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">17.21</td>
    <td align="right">13.70</td>
    <td align="right">15.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">78.63</td>
    <td align="right">63.42</td>
    <td align="right">37.51</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">16.86</td>
    <td align="right">14.99</td>
    <td align="right">13.25</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">28.42</td>
    <td align="right">27.63</td>
    <td align="right">29.12</td>
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
    <td align="right">7.61</td>
    <td align="right">9.07</td>
    <td align="right">10.48</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.12</td>
    <td align="right">5.92</td>
    <td align="right">4.59</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.96</td>
    <td align="right">7.49</td>
    <td align="right">6.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">9.41</td>
    <td align="right">9.62</td>
    <td align="right">10.86</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">8.82</td>
    <td align="right">10.07</td>
    <td align="right">12.35</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">13.74</td>
    <td align="right">15.59</td>
    <td align="right">17.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">18.56</td>
    <td align="right">22.20</td>
    <td align="right">17.04</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.23</td>
    <td align="right">15.98</td>
    <td align="right">12.86</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">28.19</td>
    <td align="right">21.97</td>
    <td align="right">22.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">18.80</td>
    <td align="right">20.23</td>
    <td align="right">12.32</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">11.44</td>
    <td align="right">10.20</td>
    <td align="right">9.27</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">18.59</td>
    <td align="right">21.41</td>
    <td align="right">15.75</td>
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
    <td align="right">34.40</td>
    <td align="right">5.66</td>
    <td align="right">3.52</td>
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
    <td align="right">11.95</td>
    <td align="right">12.55</td>
    <td align="right">17.11</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.80</td>
    <td align="right">4.19</td>
    <td align="right">4.25</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.85</td>
    <td align="right">5.55</td>
    <td align="right">5.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.19</td>
    <td align="right">17.56</td>
    <td align="right">17.68</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.88</td>
    <td align="right">4.74</td>
    <td align="right">4.79</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.59</td>
    <td align="right">8.47</td>
    <td align="right">8.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.47</td>
    <td align="right">21.16</td>
    <td align="right">17.07</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.59</td>
    <td align="right">5.65</td>
    <td align="right">5.28</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.41</td>
    <td align="right">10.90</td>
    <td align="right">10.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.81</td>
    <td align="right">26.87</td>
    <td align="right">17.02</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.90</td>
    <td align="right">5.90</td>
    <td align="right">5.86</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">19.47</td>
    <td align="right">14.25</td>
    <td align="right">14.32</td>
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
    <td align="right">8.87</td>
    <td align="right">10.00</td>
    <td align="right">10.01</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.92</td>
    <td align="right">5.16</td>
    <td align="right">5.22</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">11.68</td>
    <td align="right">5.57</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.87</td>
    <td align="right">4.93</td>
    <td align="right">4.10</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.03</td>
    <td align="right">5.79</td>
    <td align="right">5.99</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.34</td>
    <td align="right">8.75</td>
    <td align="right">8.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">8.36</td>
    <td align="right">10.13</td>
    <td align="right">5.44</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.28</td>
    <td align="right">6.61</td>
    <td align="right">6.57</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.01</td>
    <td align="right">10.43</td>
    <td align="right">10.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">9.30</td>
    <td align="right">9.89</td>
    <td align="right">5.63</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.32</td>
    <td align="right">7.38</td>
    <td align="right">7.39</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.85</td>
    <td align="right">12.57</td>
    <td align="right">13.43</td>
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
    <td align="right">39.94</td>
    <td align="right">19.98</td>
    <td align="right">7.04</td>
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
    <td align="right">14.33</td>
    <td align="right">13.10</td>
    <td align="right">17.82</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.00</td>
    <td align="right">4.45</td>
    <td align="right">4.50</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.28</td>
    <td align="right">6.25</td>
    <td align="right">6.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.23</td>
    <td align="right">19.25</td>
    <td align="right">18.56</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.55</td>
    <td align="right">5.11</td>
    <td align="right">5.06</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.70</td>
    <td align="right">9.84</td>
    <td align="right">10.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">29.11</td>
    <td align="right">24.89</td>
    <td align="right">18.09</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.29</td>
    <td align="right">5.88</td>
    <td align="right">5.79</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">18.08</td>
    <td align="right">12.86</td>
    <td align="right">13.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">53.37</td>
    <td align="right">53.09</td>
    <td align="right">19.92</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.94</td>
    <td align="right">7.40</td>
    <td align="right">7.52</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">24.35</td>
    <td align="right">17.97</td>
    <td align="right">19.45</td>
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
    <td align="right">8.99</td>
    <td align="right">10.15</td>
    <td align="right">10.09</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.88</td>
    <td align="right">5.51</td>
    <td align="right">5.55</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">11.93</td>
    <td align="right">6.28</td>
    <td align="right">6.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.15</td>
    <td align="right">5.27</td>
    <td align="right">4.43</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.19</td>
    <td align="right">6.32</td>
    <td align="right">6.36</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.51</td>
    <td align="right">9.27</td>
    <td align="right">9.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.71</td>
    <td align="right">10.58</td>
    <td align="right">6.02</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.99</td>
    <td align="right">7.67</td>
    <td align="right">7.54</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.47</td>
    <td align="right">11.50</td>
    <td align="right">11.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">11.46</td>
    <td align="right">12.60</td>
    <td align="right">8.11</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">14.04</td>
    <td align="right">10.52</td>
    <td align="right">10.62</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">22.83</td>
    <td align="right">15.22</td>
    <td align="right">16.31</td>
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
    <td align="right">61.36</td>
    <td align="right">30.44</td>
    <td align="right">13.61</td>
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
    <td align="right">27.55</td>
    <td align="right">42.29</td>
    <td align="right">36.66</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.96</td>
    <td align="right">16.19</td>
    <td align="right">16.07</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.36</td>
    <td align="right">20.60</td>
    <td align="right">20.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.50</td>
    <td align="right">64.77</td>
    <td align="right">39.38</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.38</td>
    <td align="right">19.42</td>
    <td align="right">19.33</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.48</td>
    <td align="right">26.81</td>
    <td align="right">26.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.87</td>
    <td align="right">78.84</td>
    <td align="right">38.45</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.43</td>
    <td align="right">18.59</td>
    <td align="right">18.49</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.24</td>
    <td align="right">33.17</td>
    <td align="right">33.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">53.44</td>
    <td align="right">91.58</td>
    <td align="right">35.82</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">17.38</td>
    <td align="right">18.63</td>
    <td align="right">18.61</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">33.98</td>
    <td align="right">36.28</td>
    <td align="right">36.29</td>
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
    <td align="right">10.61</td>
    <td align="right">13.71</td>
    <td align="right">13.71</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.25</td>
    <td align="right">19.71</td>
    <td align="right">19.70</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.83</td>
    <td align="right">22.21</td>
    <td align="right">22.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.90</td>
    <td align="right">16.63</td>
    <td align="right">16.00</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.27</td>
    <td align="right">18.59</td>
    <td align="right">18.64</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.97</td>
    <td align="right">29.20</td>
    <td align="right">29.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.54</td>
    <td align="right">19.60</td>
    <td align="right">19.76</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.27</td>
    <td align="right">18.68</td>
    <td align="right">18.38</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.28</td>
    <td align="right">45.97</td>
    <td align="right">46.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">23.11</td>
    <td align="right">24.25</td>
    <td align="right">24.31</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.21</td>
    <td align="right">19.63</td>
    <td align="right">19.64</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">76.55</td>
    <td align="right">54.47</td>
    <td align="right">54.42</td>
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
    <td align="right">72.38</td>
    <td align="right">104.20</td>
    <td align="right">18.36</td>
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
    <td align="right">27.52</td>
    <td align="right">42.65</td>
    <td align="right">39.14</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.83</td>
    <td align="right">16.16</td>
    <td align="right">16.40</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.54</td>
    <td align="right">20.59</td>
    <td align="right">20.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">35.93</td>
    <td align="right">61.02</td>
    <td align="right">40.65</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.27</td>
    <td align="right">19.58</td>
    <td align="right">19.45</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.32</td>
    <td align="right">25.91</td>
    <td align="right">25.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">44.17</td>
    <td align="right">77.55</td>
    <td align="right">39.05</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">17.53</td>
    <td align="right">18.93</td>
    <td align="right">19.49</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">30.67</td>
    <td align="right">34.67</td>
    <td align="right">34.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">63.59</td>
    <td align="right">104.73</td>
    <td align="right">42.01</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">20.71</td>
    <td align="right">21.85</td>
    <td align="right">22.53</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">40.27</td>
    <td align="right">43.03</td>
    <td align="right">44.52</td>
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
    <td align="right">10.74</td>
    <td align="right">13.77</td>
    <td align="right">13.78</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.34</td>
    <td align="right">19.90</td>
    <td align="right">19.90</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.00</td>
    <td align="right">22.49</td>
    <td align="right">22.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.61</td>
    <td align="right">16.18</td>
    <td align="right">15.53</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.04</td>
    <td align="right">19.00</td>
    <td align="right">18.82</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.97</td>
    <td align="right">29.32</td>
    <td align="right">29.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">14.56</td>
    <td align="right">19.74</td>
    <td align="right">19.74</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">18.64</td>
    <td align="right">19.62</td>
    <td align="right">18.70</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">65.14</td>
    <td align="right">48.25</td>
    <td align="right">48.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">29.82</td>
    <td align="right">31.90</td>
    <td align="right">33.52</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">22.57</td>
    <td align="right">23.25</td>
    <td align="right">24.70</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">86.58</td>
    <td align="right">61.40</td>
    <td align="right">61.13</td>
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
    <td align="right">63.98</td>
    <td align="right">10.23</td>
    <td align="right">7.06</td>
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
    <td align="right">13.74</td>
    <td align="right">22.88</td>
    <td align="right">26.73</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.84</td>
    <td align="right">12.51</td>
    <td align="right">12.50</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.93</td>
    <td align="right">16.16</td>
    <td align="right">16.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.66</td>
    <td align="right">35.50</td>
    <td align="right">29.34</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.27</td>
    <td align="right">14.26</td>
    <td align="right">14.23</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.39</td>
    <td align="right">22.40</td>
    <td align="right">22.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.58</td>
    <td align="right">47.47</td>
    <td align="right">30.18</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.78</td>
    <td align="right">15.66</td>
    <td align="right">15.52</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.13</td>
    <td align="right">32.33</td>
    <td align="right">32.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">33.47</td>
    <td align="right">60.43</td>
    <td align="right">30.39</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.70</td>
    <td align="right">16.46</td>
    <td align="right">16.45</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">30.41</td>
    <td align="right">37.26</td>
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
    <td align="right">7.03</td>
    <td align="right">9.39</td>
    <td align="right">9.66</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.81</td>
    <td align="right">13.99</td>
    <td align="right">13.94</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.24</td>
    <td align="right">16.77</td>
    <td align="right">16.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.84</td>
    <td align="right">14.00</td>
    <td align="right">14.03</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.57</td>
    <td align="right">15.51</td>
    <td align="right">15.51</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.83</td>
    <td align="right">22.29</td>
    <td align="right">22.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.82</td>
    <td align="right">17.56</td>
    <td align="right">17.58</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.75</td>
    <td align="right">16.85</td>
    <td align="right">16.86</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.80</td>
    <td align="right">30.99</td>
    <td align="right">30.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">17.15</td>
    <td align="right">21.96</td>
    <td align="right">21.94</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">16.07</td>
    <td align="right">17.97</td>
    <td align="right">17.99</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.27</td>
    <td align="right">36.03</td>
    <td align="right">36.04</td>
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
    <td align="right">76.47</td>
    <td align="right">45.82</td>
    <td align="right">12.32</td>
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
    <td align="right">14.60</td>
    <td align="right">23.44</td>
    <td align="right">28.54</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.76</td>
    <td align="right">12.73</td>
    <td align="right">12.70</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.31</td>
    <td align="right">17.07</td>
    <td align="right">16.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.60</td>
    <td align="right">34.80</td>
    <td align="right">29.81</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">11.95</td>
    <td align="right">13.85</td>
    <td align="right">13.90</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">16.93</td>
    <td align="right">22.02</td>
    <td align="right">22.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">25.11</td>
    <td align="right">48.14</td>
    <td align="right">30.17</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">14.14</td>
    <td align="right">15.58</td>
    <td align="right">15.58</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.51</td>
    <td align="right">34.04</td>
    <td align="right">34.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">39.15</td>
    <td align="right">67.10</td>
    <td align="right">37.10</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">27.16</td>
    <td align="right">28.13</td>
    <td align="right">42.39</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">50.56</td>
    <td align="right">51.92</td>
    <td align="right">56.75</td>
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
    <td align="right">7.45</td>
    <td align="right">9.90</td>
    <td align="right">9.82</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">12.61</td>
    <td align="right">14.35</td>
    <td align="right">14.40</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">14.17</td>
    <td align="right">18.19</td>
    <td align="right">18.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.16</td>
    <td align="right">14.74</td>
    <td align="right">14.79</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.88</td>
    <td align="right">15.53</td>
    <td align="right">16.53</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.20</td>
    <td align="right">22.18</td>
    <td align="right">21.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">13.37</td>
    <td align="right">17.16</td>
    <td align="right">17.39</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">14.76</td>
    <td align="right">16.93</td>
    <td align="right">17.07</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">26.71</td>
    <td align="right">32.48</td>
    <td align="right">31.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">18.94</td>
    <td align="right">24.53</td>
    <td align="right">25.08</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">18.33</td>
    <td align="right">23.90</td>
    <td align="right">25.41</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">36.05</td>
    <td align="right">37.89</td>
    <td align="right">38.13</td>
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
    <td align="right">42.12</td>
    <td align="right">8.92</td>
    <td align="right">6.84</td>
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
    <td align="right">55.33</td>
    <td align="right">53.56</td>
    <td align="right">36.92</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.05</td>
    <td align="right">17.31</td>
    <td align="right">20.50</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.97</td>
    <td align="right">41.55</td>
    <td align="right">41.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">84.70</td>
    <td align="right">77.80</td>
    <td align="right">38.31</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">20.32</td>
    <td align="right">18.66</td>
    <td align="right">20.64</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">24.71</td>
    <td align="right">56.74</td>
    <td align="right">57.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">104.46</td>
    <td align="right">96.58</td>
    <td align="right">37.28</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">21.66</td>
    <td align="right">19.23</td>
    <td align="right">20.60</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">36.26</td>
    <td align="right">77.02</td>
    <td align="right">77.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">134.30</td>
    <td align="right">120.59</td>
    <td align="right">37.93</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">23.57</td>
    <td align="right">20.32</td>
    <td align="right">21.10</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">41.75</td>
    <td align="right">91.47</td>
    <td align="right">91.94</td>
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
    <td align="right">18.86</td>
    <td align="right">28.86</td>
    <td align="right">28.86</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">21.73</td>
    <td align="right">23.07</td>
    <td align="right">24.94</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">22.95</td>
    <td align="right">40.14</td>
    <td align="right">41.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">15.96</td>
    <td align="right">32.55</td>
    <td align="right">23.76</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">23.60</td>
    <td align="right">23.61</td>
    <td align="right">25.40</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">28.86</td>
    <td align="right">56.67</td>
    <td align="right">58.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">26.50</td>
    <td align="right">52.89</td>
    <td align="right">37.01</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">26.44</td>
    <td align="right">26.60</td>
    <td align="right">27.31</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">41.45</td>
    <td align="right">77.98</td>
    <td align="right">78.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0262</td>
    <td align="right">25.97</td>
    <td align="right">50.99</td>
    <td align="right">38.04</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">27.25</td>
    <td align="right">29.91</td>
    <td align="right">29.38</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">47.54</td>
    <td align="right">91.75</td>
    <td align="right">92.37</td>
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
    <td align="right">64.43</td>
    <td align="right">38.80</td>
    <td align="right">20.47</td>
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
    <td align="right">61.91</td>
    <td align="right">57.14</td>
    <td align="right">41.06</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">21.61</td>
    <td align="right">17.96</td>
    <td align="right">22.67</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">22.08</td>
    <td align="right">42.72</td>
    <td align="right">41.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">96.21</td>
    <td align="right">85.08</td>
    <td align="right">42.24</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">24.59</td>
    <td align="right">19.22</td>
    <td align="right">22.52</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">26.38</td>
    <td align="right">57.31</td>
    <td align="right">58.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">117.87</td>
    <td align="right">104.01</td>
    <td align="right">42.44</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">25.03</td>
    <td align="right">31.17</td>
    <td align="right">30.64</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">42.88</td>
    <td align="right">81.92</td>
    <td align="right">90.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">173.86</td>
    <td align="right">225.33</td>
    <td align="right">45.86</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">33.79</td>
    <td align="right">26.56</td>
    <td align="right">28.74</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">48.49</td>
    <td align="right">98.59</td>
    <td align="right">99.48</td>
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
    <td align="right">20.78</td>
    <td align="right">34.27</td>
    <td align="right">34.87</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">24.60</td>
    <td align="right">24.92</td>
    <td align="right">28.35</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">26.14</td>
    <td align="right">41.69</td>
    <td align="right">43.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">18.04</td>
    <td align="right">40.27</td>
    <td align="right">36.45</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">27.97</td>
    <td align="right">27.73</td>
    <td align="right">28.71</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">53.02</td>
    <td align="right">60.56</td>
    <td align="right">64.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">31.35</td>
    <td align="right">65.40</td>
    <td align="right">48.51</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">31.68</td>
    <td align="right">33.05</td>
    <td align="right">31.49</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">45.99</td>
    <td align="right">79.73</td>
    <td align="right">80.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">34.70</td>
    <td align="right">67.11</td>
    <td align="right">51.94</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">45.23</td>
    <td align="right">43.53</td>
    <td align="right">37.44</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">56.95</td>
    <td align="right">100.41</td>
    <td align="right">107.70</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
